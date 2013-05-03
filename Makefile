check:
	pep8 move move.py setup.py
	pep257 move move.py setup.py
	pylint --report=no --include-ids=yes --disable=C0103,R0914,W0622 --rcfile=/dev/null move.py setup.py
	python setup.py --long-description | rst2html --strict > /dev/null
	scspell move move.py setup.py README.rst

readme:
	@restview --long-description

register:
	@python setup.py register sdist upload
	@srm ~/.pypirc
