# Insta Parser Project

This project is a Django-based application for parsing Instagram data. It includes Docker support for containerization and uses Celery for task management.

## Prerequisites

- Docker

## Setup

**Build container** :

```shell
docker build -t parser -f docker/Dockerfile .
```
**Start the Docker containers**:
```shell
docker-compose -p parser -f docker/docker-compose.yaml up -d	
```

## Environment Variables
* REDIS_HOST: Redis host (default: 127.0.0.1)
* REDIS_PORT: Redis port (default: 6379)
* TELEGRAM_BOT_TOKEN: Telegram bot token
* CHAT_ID: Telegram chat ID

## Access the Django application: 
Open your web browser and navigate to the address where your Django application is running. By default, it should be accessible at http://localhost:8000.
## Example

http://127.0.0.1:8000/api/scrape/?username=nasa&hashtag=Space
## Configure Celery: 
Celery needs to be configured through the Django admin interface. Navigate to http://localhost:8000/admin and configure the necessary Celery settings.

