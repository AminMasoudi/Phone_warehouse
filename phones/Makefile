.DEFAULT_GOAL := run
SHELL := /bin/bash 
SECRET_KEY ?= $(shell bash -c 'read -p "SECRET_KEY: " SECRET_KEY; echo $$SECRET_KEY')

install:
	@pip install -r req.pip

run: export DEBUG=True
run: migrate
	@./manage.py runserver

test: migrate
	@./manage.py test

migrate: install
	@./manage.py makemigrations
	@./manage.py migrate

deploy: instal
	@clear
	@echo $(SECRET_KEY) > /dev/null
	@echo "[RUNNING]"
	@gunicorn grito.wsgi