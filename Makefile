build:
	@poetry build

publish:
	@poetry publish --dry-run --username BIBA --password BUBA

RE:
	@python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	@poetry run flake8 gendiff

selfcheck:
	poetry check

check: 
	selfcheck test lint

check-coverage:
	poetry run pytest --cov=gendiff --cov-report=term-missing --cov-report=xml