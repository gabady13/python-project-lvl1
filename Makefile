install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

package-install:
	pip install dist/*.whl

