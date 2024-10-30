install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py test_*.py *.py
format:
	black *.py
test:
	pytest --nbval test_*.py
	pytest --nbval-lax *.ipynb


all: install lint format test
