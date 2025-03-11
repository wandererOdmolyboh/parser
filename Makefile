build:
	docker build -t parser -f docker/Dockerfile .

up:
	docker-compose -p parser -f docker/docker-compose.yaml up -d

start:
	docker-compose -p parser -f docker/docker-compose.yaml start

stop:
	docker-compose -p parser -f docker/docker-compose.yaml stop

clean:
	docker-compose -p parser -f docker/docker-compose.yaml down
