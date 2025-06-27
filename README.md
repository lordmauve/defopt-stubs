# types-defopt

Typing stubs for the [defopt](https://github.com/anntzer/defopt) package.

These stubs provide type hints for the runtime library, which does not
ship with annotations. Only the minimal API used by typical scripts is
covered. Contributions to improve coverage are welcome.

## Installation

```
pip install types-defopt
```

## Development

Stubs are located under `stubs/defopt`. Use the provided `Makefile`
to validate them within an isolated environment:

```
make test
```

This creates a virtual environment, installs the runtime library and the
stubs, and then type-checks both the stubs and an example script. The CI
workflow performs the same check.

## Publishing

Releases are automated via GitHub Actions. Create a git tag starting
with `v` (e.g. `v0.1.0`) and push it to trigger a PyPI upload. A
`PYPI_TOKEN` secret must be configured in the repository settings.
