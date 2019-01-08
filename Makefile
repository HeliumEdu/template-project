.PHONY: all install clean test

SHELL := /usr/bin/env bash

all: install clean test

install:
	python3 -m pip install heliumcli virtualenv

clean:
	rm -rf build

test: clean
	mkdir build
	cd build && helium-cli init template-project-test-build "Template Project Test Build" test.com heliumedu
	python3 -m virtualenv build/template-project-test-build/.venv
	( \
		source build/template-project-test-build/.venv/bin/activate; \
		python -m pip install -r build/template-project-test-build/requirements.txt; \
	)
	make -C build/template-project-test-build env test
