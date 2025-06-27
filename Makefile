
.PHONY: test clean sync

PYTHON=python3
MYPY=mypy

clean:
	rm -rf .mypy_cache

sync:
	uv sync --active --group dev --offline --no-install-package mypy

# Run mypy on stubs and example script
mypy: sync
	$(MYPY) --strict --package defopt tests/test_script.py

test: mypy
	$(PYTHON) tests/test_script.py 42 --times 1
