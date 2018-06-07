all: build

build: image-build
	mkdir -p dist
	docker-compose run --rm build

image-build:
	docker-compose build

clean:
	rm -rf dist
