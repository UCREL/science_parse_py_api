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

docker_docs_serve:
	nbdev_build_docs
	cd docs
	docker-compose up --build
	docker-compose down

test:
	python -m pytest --cov=science_parse_api --cov-report term-missing --cov-report xml --cov-config .coveragerc

release: 
	python -m build
	python -m twine upload --repository pypi --config-file ./.pypirc dist/*

conda_release:
	fastrelease_conda_package

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist