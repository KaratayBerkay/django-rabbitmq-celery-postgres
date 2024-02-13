FROM python:3.8.2

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /jangoapp

COPY requirements.txt /jangoapp/requirements.txt
COPY entrypoint.sh /jangoapp/entrypoint.sh

WORKDIR /jangoapp

COPY . /jangoapp

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /jangoapp/requirements.txt --upgrade

RUN chmod +x /jangoapp/entrypoint.sh
