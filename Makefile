install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user --force-reinstall dist/hexlet_code-0.1.0-py3-none-any.whl
check:
	poetry run pytest
	poetry run flake8 gendiff
test-coverage:
	poetry run coverage run -m pytest tests/test_genddiff.py
	poetry run coverage report -m tests/test_genddiff.py
