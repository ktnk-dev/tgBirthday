FROM python:3.11-slim

WORKDIR /app
COPY . /app/

RUN apt-get update && \
    apt-get install -y --no-install-recommends locales && \
    sed -i '/^#.* ru_RU.UTF-8 /s/^#//' /etc/locale.gen && \
    locale-gen && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]