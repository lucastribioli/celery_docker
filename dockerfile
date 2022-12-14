FROM python:3.9
ADD requirements.txt /app/requirements.txt
ADD ./celery/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A teste worker --concurrency=20 --loglevel=info