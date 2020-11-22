SHELL := /bin/bash

runserver:
	docker exec -it backend python ./src/manage.py runserver 0:9000

makemigrations:
	docker exec -it backend python ./src/manage.py makemigrations

migrate:
	docker exec -it backend python ./src/manage.py migrate

collectstatic:
	docker exec -it backend python ./src/manage.py collectstatic --noinput && \
	docker cp backend:/tmp/static_content/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static

start:
	cp -n .env.example .env && docker-compose up -d --build

build: start migrate collectstatic
