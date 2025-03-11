FROM python:3.10-alpine

COPY ./requirements.txt /requirements.txt

RUN apk add --no-cache --virtual .build-deps gcc g++ libc-dev make postgresql-dev libffi-dev \
    && apk add --no-cache chromium chromium-chromedriver \
    && pip install --no-cache-dir -r /requirements.txt

COPY ./docker/start-reload.sh /docker-entrypoint-initdb.d/

WORKDIR /app

ENV PYTHONPATH=/app
ENV CHROME_DRIVER_PATH=/usr/bin/chromedriver

EXPOSE 8000

CMD ["/docker-entrypoint-initdb.d/start-reload.sh"]
