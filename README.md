![Python Versions](https://img.shields.io/badge/python-%203.8%20|%203.9%20|%203.10%20|%203.11%20-blue)
[![Coverage](https://img.shields.io/codecov/c/github/HeliumEdu/template-project)](https://codecov.io/gh/HeliumEdu/template-project)
[![Build](https://img.shields.io/github/actions/workflow/status/HeliumEdu/template-project/build.yml)](https://github.com/HeliumEdu/template-project/actions/workflows/build.yml)
![GitHub License](https://img.shields.io/github/license/HeliumEdu/template-project)

# template-project

## Getting Started

The project is developed using Python and [Django](https://www.djangoproject.com).

This repository contains the source code for the HeliumEdu `template-project`, which can be initialized using
[`helium-cli`](https://github.com/HeliumEdu/heliumcli) with:

```
helium-cli init <project_id> <Project Name> <hostname> <githuber_username>
```

### Project Setup

To setup the Python/Django build environment, execute:

```sh
make install
```

This project is configured to work with a Virtualenv which has now been setup in the `venv` folder. If you're
unfamiliar with how this works, [read up on Virtualenv here](https://virtualenv.pypa.io/en/stable). The short version
is, virtualenv creates isolated environments for each project's dependencies. To activate and use this environment when
developing, execute:

```sh
source venv/bin/activate
```

All commands below will now be run within the virtualenv (though `make` commands will always automatically enter the
virtualenv before executing).

To ensure the database is in sync with the latest schema, database migrations are generated and run with Django. To run
migrations, execute:

```sh
make migrate
```

Once migrations have been run, you can create a super user, which is a standard user that also has access to the /admin
site.

```sh
python manage.py createsuperuser
```

Before commits are made, be sure to run tests and check the generated coverage report.

```sh
make test
```

Now you're all set! To start the development server, execute:

```sh
bin/runserver
```

A development server will be started at <http://localhost:8000>, though there is no mounted root URL—visit
<http://localhost:8000/admin> or <http://localhost:8000/info> to see the project serve a request.

If the `USE_NGROK` environment variable is set when a dev server is started (using `runserver`),
[pyngrok](https://github.com/alexdlaird/pyngrok) will be used to open a `ngrok` tunnel. This is especially useful when
using webhooks.
