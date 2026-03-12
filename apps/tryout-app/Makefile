ROOT_DIR := $(abspath ../..)
IMAGE_NAME ?= tryout-app:latest
DOCKERFILE := $(CURDIR)/Dockerfile

.PHONY: docker-build docker-run run test

# Build the tryout-app Docker image from the repository root context.
docker-build:
	docker build -f $(DOCKERFILE) -t $(IMAGE_NAME) $(ROOT_DIR)

# Run the tryout-app container and remove it when it exits.
docker-run:
	docker run --rm $(IMAGE_NAME)

# Run tryout-app locally.
run:
	cd $(ROOT_DIR) && uv run --package tryout-app python -m tryout_app.main

# Run tryout-app tests locally.
test:
	cd $(ROOT_DIR) && ./pants test apps/tryout-app/tests::
