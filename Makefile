.PHONY: test clean sync

PYTHON=.venv/bin/python
MYPY=mypy

clean:
	rm -rf .mypy_cache

sync:
	uv sync --active --group dev --no-install-package mypy

# Run mypy on stubs and example script
mypy: sync
	$(MYPY) --strict stubs/defopt tests/test_script.py

test: mypy
	$(PYTHON) tests/test_script.py 42 --times 1
