FROM python:3-alpine

MAINTAINER Jean Souza <jean.azuos@gmail.com>

COPY app.py /app/
COPY pigeon_news /app/pigeon_news
COPY requirements.txt /app/
COPY scrapy.cfg /app/

WORKDIR /app

RUN apk update && \
  apk add --no-cache \
    gcc \
    linux-headers \
    musl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    openssl-dev \
    python3-dev \
    python3 && \
    pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]