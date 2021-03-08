.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard ./*.ipynb)

all: science_parse_py_api docs

science_parse_py_api: $(SRC)
	nbdev_build_lib
	touch science_parse_py_api

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docker_docs_serve: docs
	cd docs && docker-compose up --build && docker-compose down

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi conda_release
	nbdev_bump_version

conda_release:
	fastrelease_conda_package

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist