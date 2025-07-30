
.PHONY: test clean sync

PYTHON=.venv/bin/python
MYPY=.venv/bin/mypy

clean:
	rm -rf .mypy_cache

sync:
	uv sync --group dev

# Run mypy on stubs and example script
mypy: sync
	$(MYPY) --strict stubs/defopt-stubs tests/test_script.py

test: mypy
	$(PYTHON) tests/test_script.py 42 --times 1
