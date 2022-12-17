from __future__ import absolute_import
from celery import app
import time, requests
from pymongo import MongoClient


client = MongoClient('10.1.1.234', 27018)
db = client.mongodb_test
collection = db.celery
post = db.test


#default_retry_delay atua como um sleep, para simular uma tarefa demorada nesse caso
@app.task(bind=True, default_retry_delay=10) 
def longtime_add(self,i):
    print('Começou a processar a tarefa')
    try:
        r = requests.get(i)
        post.insert({'status':r.status_code,"creat_time":time.time()})
        print('Terminou a tarefa')
    except Exception as exc:
        raise self.retry(exc=exc)
    return r.status_code