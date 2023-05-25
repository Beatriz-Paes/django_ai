# Exported variables for subshells, and their default values
export PYTHONPATH 	:= $(PWD)

# Loading .env if exists. This file can override the variables above.
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

.PHONY: pylint
# Run Pylint inside Docker.
pylint:
	@echo "Running PyLint..."
	@pylint core proposals_api

.PHONY: black
# Run Black inside Docker.
black:
	@echo "Running Black..."
	@black --check .

.PHONY: precommit
# Run Pre-Commit inside Docker.
pre-commit:
	@echo "Running Pre-Commit..."
	@pre-commit install -f
	@pre-commit run --all
