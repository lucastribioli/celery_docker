from __future__ import absolute_import
from celery import Celery

# Primeiro argumento é o nome do módulo, segundo é o nome da fila, terceiro é o result backend (é onde é armazenado o que a tarefa vai retornar)
app = Celery('teste',broker='amqp://admin:mypass@rabbit:5672',backend='rpc://',include=['celery.tasks'])
