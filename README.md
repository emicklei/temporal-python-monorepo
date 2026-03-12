# temporal-python-mono

[![Build Status](https://github.com/emicklei/temporal-python-monorepo/actions/workflows/ci-tests-coverage-and-app-image.yml/badge.svg?branch=main)](https://github.com/emicklei/temporal-python-monorepo/actions/workflows/ci-tests-coverage-and-app-image.yml)
[![Coverage](https://codecov.io/gh/emicklei/temporal-python-monorepo/branch/main/graph/badge.svg)](https://codecov.io/gh/emicklei/temporal-python-monorepo)

Python monorepo scaffolded with `uv` and `pants`.

## Structure

- `apps/`: application projects
- `pkgs/`: shared reusable packages
- `pkgs/converters`: shared package exposing `DegreesToFahrenheit`
- `pkgs/quotes`: shared package exposing scientist quotes
- `apps/demo-app`: demo application using `converters` and `quotes`

## Setup

From the repository root:

```bash
uv sync --all-packages
chmod +x ./pants
uv python install 3.9
```

Pants 2.17 boots with Python 3.9 and runs tests with Python 3.11 in this repository.

## Demo App Commands

The demo app has its own Makefile at `apps/demo-app/Makefile`.

From `apps/demo-app`:

```bash
make run
make test
make docker-build
make docker-run
```

Expected output for `make run`:

```text
24 degrees Celsius is 75.2 Fahrenheit
```

## Run All Tests

```bash
PYTHON=python3.9 ./pants test ::
```

or simply:

```bash
./pants test ::
```

## Run Changed Tests

Run only tests affected by changes compared to `origin/main`:

```bash
PYTHON=python3.9 ./pants --changed-since=origin/main --changed-dependents=transitive test
```

## Coverage

Generate coverage with Pants:

```bash
PYTHON=python3.9 ./pants test --use-coverage ::
```

Reports are written to:

- `dist/coverage/python/coverage.xml`
- `dist/coverage/python/htmlcov/`

## Pre-commit Hook: Tag Validation

This repository includes a local `pre-commit` hook that validates git tags follow:

```text
apps/<folder>/vX.Y.Z
```

Rules:

- `<folder>` must exist under `apps/`
- `X`, `Y`, and `Z` must be non-negative integers (`>= 0`)

Install and run:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```
