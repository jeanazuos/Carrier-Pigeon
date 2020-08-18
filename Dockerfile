FROM python:3-alpine

MAINTAINER Jean Souza <jean.azuos@gmail.com>

COPY app.py /app
COPY pigeon_news /app
COPY requirements.txt /app
COPY scrapy.cfg /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]