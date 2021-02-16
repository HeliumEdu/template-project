[![CI/CD](https://github.com/{%PROJECT_GITHUB_USER%}/{%PROJECT_ID%}/workflows/CI/CD/badge.svg)](https://github.com/{%PROJECT_GITHUB_USER%}/{%PROJECT_ID%}/actions?query=workflow%3ACI%2FCD)
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
make migrate
```

Once migrations have been run, you can create a super user, which is a standard user that also has access to the /admin site.

```sh
python manage.py createsuperuser
```

Now you're all set! To start the development server, execute:

```sh
python manage.py runserver
```

A development server will be started at <http://localhost:8000>.

If the `USE_NGROK` environment variable is set when a dev server is started (using `runserver`, [pyngrok](https://github.com/alexdlaird/pyngrok)
will be used to open a `ngrok` tunnel. This is especially useful when using webhooks.
