.PHONY: all install clean test

SHELL := /usr/bin/env bash
PYTHON_BIN ?= python
BRANCH ?= main

all: install clean test

install:
	$(PYTHON_BIN) -m pip install --upgrade heliumcli virtualenv

clean:
	rm -rf build

test: clean
	mkdir build
	cd build && HELIUMCLI_TEMPLATE_PROJECT_VERSION=$(BRANCH) helium-cli init template-project-test-build "Template Project Test Build" test.com heliumedu
	$(PYTHON_BIN) -m virtualenv build/template-project-test-build/.venv
	( \
		source build/template-project-test-build/.venv/bin/activate; \
		python -m pip install -r build/template-project-test-build/requirements.txt -r build/template-project-test-build/requirements-dev.txt; \
	)
	make -C build/template-project-test-build env test
