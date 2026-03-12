# roche-mono

Python monorepo scaffolded with `uv` and `pdm`.

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
pdm install -G dev
```

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
uv run pytest -q
```
