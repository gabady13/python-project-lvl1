install:
	@poetry install

brain-games:
	poetry run brain-game

build:
	poetry build

package-install:
	pip install dist/*.whl

lint:
	poetry run flake8 brain_games

publish:
	poetry publish --dry-run

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-progression:
	poetry run brain-progression

package-uninstall:
	pip uninstall hexlet-code
