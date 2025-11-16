#!/usr/bin/env python3
"""
Async load generator for the REST service.

Usage:
  python tools/load_test.py --url http://my-alb-dns/endpoint --concurrency 50 --duration 60

This script will spawn N concurrent workers that continuously send GET requests
to the URL for the given duration and print a short summary and periodic stats.
"""
import argparse
import asyncio
import time
import statistics
from typing import List

import aiohttp


async def worker(session: aiohttp.ClientSession, url: str, stop_at: float, stats: dict, id: int):
    while time.time() < stop_at:
        start = time.time()
        try:
            async with session.get(url, timeout=10) as resp:
                await resp.text()
                latency = time.time() - start
                stats['total'] += 1
                if 200 <= resp.status < 400:
                    stats['success'] += 1
                else:
                    stats['errors'] += 1
                stats['latencies'].append(latency)
        except Exception as e:
            stats['total'] += 1
            stats['errors'] += 1
        # small sleep to let event loop breathe; tune if you need steady RPS
        await asyncio.sleep(0)


async def run(url: str, concurrency: int, duration: int, report_interval: int = 5, ramp_up: int = 0, method: str = 'GET', payload: str = None, headers: dict | None = None):
    stats = {'total': 0, 'success': 0, 'errors': 0, 'latencies': []}
    timeout = aiohttp.ClientTimeout(total=30)
    stop_at = time.time() + duration
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []

        # Ramp-up: start workers gradually over ramp_up seconds
        if ramp_up and ramp_up > 0 and concurrency > 1:
            interval = ramp_up / max(1, concurrency - 1)
            for i in range(concurrency):
                tasks.append(asyncio.create_task(worker(session, url, stop_at, stats, i)))
                await asyncio.sleep(interval)
        else:
            tasks = [asyncio.create_task(worker(session, url, stop_at, stats, i)) for i in range(concurrency)]

        next_report = time.time() + report_interval
        while time.time() < stop_at:
            await asyncio.sleep(1)
            if time.time() >= next_report:
                total = stats['total']
                succ = stats['success']
                err = stats['errors']
                lat = stats['latencies']
                mean = statistics.mean(lat) if lat else 0
                p95 = statistics.quantiles(lat, n=100)[94] if len(lat) >= 100 else (max(lat) if lat else 0)
                print(f"t={int(time.time())} total={total} success={succ} errors={err} mean_ms={mean*1000:.1f} p95_ms={p95*1000:.1f}")
                next_report = time.time() + report_interval

        await asyncio.gather(*tasks, return_exceptions=True)

    # Final report
    total = stats['total']
    succ = stats['success']
    err = stats['errors']
    lat = stats['latencies']
    mean = statistics.mean(lat) if lat else 0
    p50 = statistics.median(lat) if lat else 0
    p95 = statistics.quantiles(lat, n=100)[94] if len(lat) >= 100 else (max(lat) if lat else 0)
    print('\n=== Final report ===')
    print(f'Total requests: {total}')
    print(f'Successful: {succ}')
    print(f'Errors: {err}')
    print(f'Mean latency ms: {mean*1000:.1f}')
    print(f'P50 ms: {p50*1000:.1f}, P95 ms: {p95*1000:.1f}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help='Target URL to hit')
    parser.add_argument('--concurrency', type=int, default=50)
    parser.add_argument('--duration', type=int, default=60, help='Duration in seconds')
    parser.add_argument('--report-interval', type=int, default=5)
    args = parser.parse_args()

    asyncio.run(run(args.url, args.concurrency, args.duration, args.report_interval))


if __name__ == '__main__':
    main()
