check:
	pep8 move move.py setup.py qmv-move-helper
	pep257 move move.py setup.py qmv-move-helper
	pylint \
		--reports=no \
		--msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}' \
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
