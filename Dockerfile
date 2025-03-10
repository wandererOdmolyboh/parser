FROM python:3.11-alpine

COPY ./requirements.txt /requirements.txt

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make postgresql-dev libffi-dev \
    && pip install --no-cache-dir -r /requirements.txt \
    && apk del .build-deps gcc libc-dev make postgresql-dev libffi-dev

RUN pip install uvicorn

COPY ./docker/start-reload.sh /docker-entrypoint-initdb.d/

WORKDIR /app

ENV PYTHONPATH=/app

EXPOSE 8000

COPY ./src/ /app/

ENTRYPOINT ["python3"]

CMD ["-m", "uvicorn", "settings.asgi:application"]
