# defopt-stubs

Typing stubs for the [defopt](https://github.com/anntzer/defopt) package.

These stubs provide type hints for the runtime library, which does not
ship with annotations. Only the minimal API used by typical scripts is
covered. Contributions to improve coverage are welcome.

## Installation

```
pip install defopt-stubs
```

## Development

Stubs are located under `stubs/defopt-stubs`. Use the provided `Makefile`
and `uv` to validate them:

```
make test
```

`make test` runs `uv sync` to install development dependencies and the
runtime library before type-checking the stubs and an example script.
The CI workflow performs the same check.

## Publishing

Releases are automated via GitHub Actions. Create a git tag starting
with `v` (e.g. `v0.1.0`) and push it to trigger a PyPI upload. A
`PYPI_TOKEN` secret must be configured in the repository settings.
