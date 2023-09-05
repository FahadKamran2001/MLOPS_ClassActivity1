install:
	pip install --upgrade pip
	pip install -r requirement.txt
lint:
	pylint --disable=C,R i200983.py
test:
	python -m pytest -vv --cov=i200983 test_i200983.py