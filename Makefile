.PHONY: clean virtualenv test docker dist dist-upload

install:
	pip3 install poetry
	poetry update
	poetry install --no-root --no-interaction --no-ansi

test:
	poetry run pytest tests --capture=no

run:
	poetry run ./main.py
