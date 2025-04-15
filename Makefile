# api setup is borrowed from https://github.com/frgfm/Holocron/blob/main/api

.PHONY: lock run stop test
# Pin the dependencies
lock:
	pip install poetry>=1.0 poetry-plugin-export
	poetry lock
	poetry export -f requirements.txt --without-hashes --output requirements.txt
	poetry export -f requirements.txt --without-hashes --with dev --output requirements-dev.txt


