.PHONY: build clean publish test
build:
	python3 -m build

publish:
	python3 -m twine upload --repository pypi dist/*

test:
	python -m unittest

clean:
	rm -fr dist
	rm -fr *.egg-info
