.PHONY: all install clean test

SHELL := /usr/bin/env bash

all: install clean test

install:
	pip install heliumcli

clean:
	rm -rf build

test: clean
	mkdir build
	cd build && helium-cli init template-project-test-build "Template Project Test Build" test.com heliumedu
	make -C build/template-project-test-build install test