.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard ./*.ipynb)

docker_docs_serve:
	nbdev_build_docs
	cd docs
	docker-compose up --build
	docker-compose down

test:
	python -m pytest --cov=science_parse_api --cov-report term-missing --cov-report xml --cov-config .coveragerc

release: clean
	python setup.py sdist bdist_wheel
	python -m twine upload --repository pypi --config-file ./.pypirc dist/*

clean:
	rm -rf build
	rm -rf dist