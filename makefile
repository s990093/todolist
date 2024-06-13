.PHONY: all test run web git clean install test-extended venv help

# Virtual environment activation command
VENV = source .venv/bin/activate

# Default target
all: run

# Test target: run unit tests
test:
	$(VENV) && python todolistserver/src/test.py

# Run target: start the main application
run:
	$(VENV) && python main.py

# Web target: start the web application
web:
	cd todolistweb && yarn dev

# Git target: add, commit, and push changes
git:
	git add .
	git commit -m "this commit"
	git push

# Clean target: remove all .pyc files and __pycache__ directories
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Install target: install required Python packages and Node modules
install:
	$(VENV) && pip install -r requirements.txt
	cd todolistweb && yarn install

# Extended test target: run unit tests with coverage and linters
test-extended: test
	$(VENV) && coverage run --source=src -m unittest discover
	$(VENV) && coverage report
	$(VENV) && flake8 src
	$(VENV) && pylint src

# Setup virtual environment
venv:
	python -m venv .venv
	$(VENV) && pip install --upgrade pip

# Help target: display available make targets
help:
	@echo "Available targets:"
	@echo "  all           - Default target, runs the main application"
	@echo "  test          - Run unit tests"
	@echo "  run           - Start the main application"
	@echo "  web           - Start the web application"
	@echo "  git           - Add, commit, and push changes"
	@echo "  clean         - Remove all .pyc files and __pycache__ directories"
	@echo "  install       - Install required Python packages and Node modules"
	@echo "  test-extended - Run extended tests with coverage and linters"
	@echo "  venv          - Setup virtual environment"
	@echo "  help          - Display this help message"
