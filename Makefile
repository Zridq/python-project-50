build:
	@poetry build

publish:
	@poetry publish --dry-run --username BIBA --password BUBA

RE:
	@python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	@poetry run flake8 gendiff