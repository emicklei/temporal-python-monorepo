ROOT_DIR := $(abspath ../..)

.PHONY: run test

# Run tryout-app locally.
run:
	cd $(ROOT_DIR) && uv run --package tryout-app python -m tryout_app.main

# Run tryout-app tests locally.
test:
	cd $(ROOT_DIR) && ./pants test apps/tryout-app/tests::
