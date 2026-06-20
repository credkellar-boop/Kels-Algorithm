.PHONY: install test simulate clean

install:
	pip install .

test:
	python3 -m unittest discover -s tests -p "test_*.py"

simulate:
	python3 src/main.py --simulate-attack

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf *.egg-info
