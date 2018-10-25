.PHONY: all env virtualenv install build build-migrations migrate test

SHELL := /usr/bin/env bash
{%PROJECT_ID_UPPER%}_VENV ?= .venv

all: env virtualenv install build migrate test

env:
	cp -n .env.example .env | true

virtualenv:
	if [ ! -d "$({%PROJECT_ID_UPPER%}_VENV)" ]; then \
		python3 -m pip install virtualenv --user; \
        python3 -m virtualenv $({%PROJECT_ID_UPPER%}_VENV); \
	fi

install: env virtualenv
	( \
		source $({%PROJECT_ID_UPPER%}_VENV)/bin/activate; \
		python -m pip install -r requirements.txt; \
	)

build: virtualenv
	( \
		source $({%PROJECT_ID_UPPER%}_VENV)/bin/activate; \
		python manage.py collectstatic --noinput; \
	)

build-migrations: env virtualenv install
	( \
		source $({%PROJECT_ID_UPPER%}_VENV)/bin/activate; \
		python manage.py makemigrations; \
	)

migrate: virtualenv
	( \
		source $({%PROJECT_ID_UPPER%}_VENV)/bin/activate; \
		python manage.py migrate; \
	)

test: virtualenv
	( \
		source $({%PROJECT_ID_UPPER%}_VENV)/bin/activate; \
		python manage.py test; \
	)