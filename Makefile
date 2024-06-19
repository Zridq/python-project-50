build:
	@poetry build

publish:
	@poetry publish --dry-run --username BIBA --password BUBA

RE:
	@python3 -m pip uninstall hexlet-code -y
	@python3 -m pip install --user dist/*.whl
	
lint:
	poetry run flake8 gendiff

test:
	@poetry run pytest

selfcheck:
	poetry check

check: 
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report=term-missing --cov-report=xml