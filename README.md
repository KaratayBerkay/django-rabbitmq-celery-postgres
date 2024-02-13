# django-rabbitmq-celery-postgres
Django api rabbitmq celey postgres implmemented
## Django with Docker with Postgres database implementation
Django with Docker with Postgres database implementation via internal and external network,
worker and broker with RabbitMQ and Celery.

Just Run with docker use:
```bash
docker compose up --build
```

Run Local commands

Install Django via cmd below:
```bash
pip install django
```

Check version of Django:
```bash
python -m django --version
```

Start App via cmd below:
```bash
django-admin startproject mysite
```

Run development server via cmd below:
```bash
python manage.py runserver 0.0.0.0:8000
```

Start a Polls app via cmd below:
```bash
python manage.py startapp polls
```





