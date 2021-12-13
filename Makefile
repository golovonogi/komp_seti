qa:
	pipenv run flake8 .
	pipenv run mypy --warn-unused-ignores .