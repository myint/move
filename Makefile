check:
	pycodestyle move move.py setup.py qmv-move-helper
	pydocstyle move move.py setup.py qmv-move-helper
	pylint \
		--reports=no \
		--rcfile=/dev/null \
		--disable=bad-whitespace \
		move.py setup.py
	python setup.py --long-description | rstcheck -
	scspell move move.py setup.py qmv-move-helper README.rst

readme:
	@restview --long-description --strict

register:
	@python setup.py register sdist upload
	@srm ~/.pypirc
