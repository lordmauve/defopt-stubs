# Contributing to defopt-stubs

Thank you for your interest in contributing to defopt-stubs! This document provides information on how to set up the development environment and contribute to the project.

## Development

Stubs are located under `stubs/defopt-stubs`. After installing development dependencies with `uv`, validate them by running `mypy`:

```
uv sync
mypy
python tests/test_script.py 42 --times 1
```

`uv sync` installs the runtime library and tooling required for type checking. The CI workflow performs the same steps.

## Publishing

Releases are automated via GitHub Actions. Create a git tag starting with `v` (e.g. `v0.1.0`) and push it to trigger a PyPI upload. A `PYPI_TOKEN` secret must be configured in the repository settings.