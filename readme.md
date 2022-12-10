# Celery com Docker

## Instalação 
---
### Docker
---
[Como instalar ?](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

### Aplicação
---
```
docker pull rabbitmq:latest

docker-compose build

docker-compose up

docker-compose scale worker=5

```