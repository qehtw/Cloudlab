FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install build deps then runtime deps
COPY requirements.txt ./
RUN apt-get update \
     && apt-get install -y --no-install-recommends \
         build-essential gcc libpq-dev default-libmysqlclient-dev curl libssl-dev libffi-dev python3-dev pkg-config \
         libxml2-dev libxslt-dev zlib1g-dev rustc cargo git wget \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn \
    && apt-get remove -y --purge build-essential gcc rustc cargo python3-dev pkg-config \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
