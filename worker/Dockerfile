FROM python:3.9.5-alpine
LABEL authors="Karatay Berkay"

WORKDIR /celery_worker

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /celery_worker/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /celery_worker
