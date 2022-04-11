SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: lint
lint:
	black --check .
	flake8 .

.PHONY: lint-fix
lint-fix:
	black .

.PHONY: deps
deps:
	pip install -r requirements.txt
