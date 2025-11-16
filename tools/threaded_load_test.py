#!/usr/bin/env python3
"""
Simple threaded load tester using requests.Session and ThreadPoolExecutor.

Usage:
  python tools/threaded_load_test.py --url http://<host>/endpoint --concurrency 100 --requests 150 --timeout 3

This will start `concurrency` worker threads; each will send `requests` HTTP GETs
to the URL (so total requests = concurrency * requests). It prints a short
summary with counts and latency percentiles.
"""
import argparse
import requests
import threading
import time
import statistics
from concurrent.futures import ThreadPoolExecutor, as_completed


def worker(session, url, req_count, timeout, stats, lock):
    for _ in range(req_count):
        start = time.perf_counter()
        try:
            r = session.get(url, timeout=timeout)
            latency = (time.perf_counter() - start)
            with lock:
                stats['total'] += 1
                stats['latencies'].append(latency)
                if 200 <= r.status_code < 400:
                    stats['success'] += 1
                else:
                    stats['errors'] += 1
        except Exception:
            with lock:
                stats['total'] += 1
                stats['errors'] += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help='Target URL')
    parser.add_argument('--concurrency', type=int, default=50, help='Number of threads')
    parser.add_argument('--requests', type=int, default=150, help='Requests per thread')
    parser.add_argument('--timeout', type=float, default=3.0, help='Per-request timeout seconds')
    parser.add_argument('--workers', type=int, default=None, help='ThreadPool max_workers (defaults to concurrency)')
    args = parser.parse_args()

    total_expected = args.concurrency * args.requests
    stats = {'total': 0, 'success': 0, 'errors': 0, 'latencies': []}
    lock = threading.Lock()

    start_all = time.perf_counter()
    with ThreadPoolExecutor(max_workers=(args.workers or args.concurrency)) as ex:
        futures = []
        for _ in range(args.concurrency):
            # use a single Session per thread for connection pooling
            session = requests.Session()
            futures.append(ex.submit(worker, session, args.url, args.requests, args.timeout, stats, lock))

        # wait for completion
        for f in as_completed(futures):
            pass

    elapsed = time.perf_counter() - start_all

    lat = stats['latencies']
    mean = statistics.mean(lat) if lat else 0
    p50 = statistics.median(lat) if lat else 0
    p95 = statistics.quantiles(lat, n=100)[94] if len(lat) >= 100 else (max(lat) if lat else 0)

    print('\n=== Final report ===')
    print(f'Target URL: {args.url}')
    print(f'Concurrency threads: {args.concurrency}')
    print(f'Requests per thread: {args.requests}')
    print(f'Total expected requests: {total_expected}')
    print(f'Total sent (observed): {stats["total"]}')
    print(f'Successful: {stats["success"]}')
    print(f'Errors: {stats["errors"]}')
    print(f'Total time sec: {elapsed:.2f}')
    print(f'Requests/sec (observed): {stats["total"]/elapsed:.1f}')
    print(f'Mean latency ms: {mean*1000:.1f}')
    print(f'P50 ms: {p50*1000:.1f}, P95 ms: {p95*1000:.1f}')


if __name__ == '__main__':
    main()
