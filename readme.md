# Celery com Docker

## Instalação 
---
### Docker
---
[Como instalar ?](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

### Aplicação
---
```
pip install -r requirements.txt

docker-compose build --no-cache

docker-compose up

celery -A celery worker -l INFO

```