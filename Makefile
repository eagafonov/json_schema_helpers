all:

test: .test-deps-installed
	coverage erase
	coverage run -m pytest -vv tests
	coverage report
	coverage html

.test-deps-installed: requirements-test.txt
	pip install -r requirements-test.txt
	touch $@

.examples-deps-installed: requirements-examples.txt
	pip install -r requirements-examples.txt
	touch $@

flake8: .test-deps-installed
	flake8
	
run_examples: .examples-deps-installed
	python examples/simple.py

