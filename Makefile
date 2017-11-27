all:

test: .test-deps-installed
	coverage erase
	coverage run -m pytest -vv tests
	coverage report
	coverage html

.test-deps-installed: requirements-test.txt
	pip install -r requirements-test.txt
	touch $@

flake8: .test-deps-installed
	flake8
