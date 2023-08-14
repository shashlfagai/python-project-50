install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl
check:
	poetry run pytest -vv
	poetry run flake8 gendiff
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
