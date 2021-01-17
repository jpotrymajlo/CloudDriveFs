init:
	pip install -r requirements

test:
    py.test tests

.PHONY: init test