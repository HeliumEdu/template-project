[![Build](https://github.com/{%PROJECT_GITHUB_USER%}/{%PROJECT_ID%}/actions/workflows/build.yml/badge.svg)](https://github.com/{%PROJECT_GITHUB_USER%}/{%PROJECT_ID%}/actions/workflows/build.yml)
![Python Versions](https://img.shields.io/badge/python-%203.6%20|%203.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11%20-blue)
![GitHub License](https://img.shields.io/github/license/{%PROJECT_GITHUB_USER%}/{%PROJECT_ID%})

# {%PROJECT_NAME%}

## Prerequisites

- Python (>= 3.6)
- Pip (>= 9.0)

## Getting Started
The project is developed using Python and [Django](https://www.djangoproject.com).

This repository contains the source code for the {%PROJECT_NAME%} project.

### Project Setup
To setup the Python/Django build environment, execute:

```sh
make install-dev
```

To ensure the database is in sync with the latest schema, database migrations are generated and run with Django. To run migrations, execute:

```sh
ENVIRONMENT=dev make migrate
```

Once migrations have been run, you can create a super user, which is a standard user that also has access to the /admin site.

```sh
ENVIRONMENT=dev python manage.py createsuperuser
```

Now you're all set! To start the development server, execute:

```sh
python manage.py runserver
```

A development server will be started at <http://localhost:8000>, though there is no mounted root URL—visit
<http://localhost:8000/admin> or <http://localhost:8000/info> to see the project serve a request.

If the `USE_NGROK` environment variable is set when a dev server is started (using `runserver`),
[pyngrok](https://github.com/alexdlaird/pyngrok) will be used to open a `ngrok` tunnel. This is especially useful when
using webhooks.
