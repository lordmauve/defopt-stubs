.PHONY: test clean

VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
MYPY=$(VENV)/bin/mypy

$(VENV):
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip mypy

clean:
	rm -rf $(VENV)
	rm -rf .mypy_cache

install: $(VENV)
	$(PIP) install defopt
	$(PIP) install .

# Run mypy on stubs and example script
mypy: install
	$(MYPY) --strict --package defopt tests/test_script.py

test: mypy
	$(PYTHON) tests/test_script.py 42 --times 1
