.PHONY: all install clean test

SHELL := /usr/bin/env bash

all: install clean test

install:
	python3 -m pip install --upgrade heliumcli virtualenv

clean:
	rm -rf build

test: clean
	mkdir build
	cd build && HELIUMCLI_TEMPLATE_PROJECT_VERSION=main helium-cli init template-project-test-build "Template Project Test Build" test.com heliumedu
	python3 -m virtualenv build/template-project-test-build/.venv
	( \
		source build/template-project-test-build/.venv/bin/activate; \
		python -m pip install -r build/template-project-test-build/requirements.txt; \
		python -m pip install -r build/template-project-test-build/requirements-dev.txt; \
	)
	make -C build/template-project-test-build env test
