SHELL := /bin/bash

manage_py := docker exec -it backend python ./src/manage.py

runserver:
	$(manage_py) runserver 0:9000

makemigrations:
	$(manage_py) makemigrations

generate_data:
	$(manage_py) generate_data

migrate:
	$(manage_py) migrate

shell:
	$(manage_py) shell_plus --print-sql

collectstatic:
	docker exec -it backend python ./src/manage.py collectstatic --noinput && \
	docker cp backend:/tmp/static_content/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static

start:
	cp -n .env.example .env && docker-compose up -d --build

build: start migrate collectstatic
