all: test

.PHONY: install
install:
	python setup.py install

.PHONY: release
release:
	python setup.py register

.PHONY: test
test:
	python setup.py test

.PHONY: clean
clean:
clean:
	rm -rf *.egg-info MANIFEST build dist
	find . -name *.pyc -exec rm {} \;
