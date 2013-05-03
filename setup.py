#!/usr/bin/env python
"""Setup for move."""

import ast
from distutils import core


def version():
    """Return version string."""
    with open('move.py') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


with open('README.rst') as readme:
    core.setup(name='move',
               version=version(),
               description='Moves revision-controlled files interactively in '
                           'an editor.',
               long_description=readme.read(),
               license='Expat License',
               author='Steven Myint',
               url='https://github.com/myint/move',
               classifiers=['Intended Audience :: Developers',
                            'Environment :: Console',
                            'Programming Language :: Python :: 2.6',
                            'Programming Language :: Python :: 2.7',
                            'Programming Language :: Python :: 3',
                            'License :: OSI Approved :: MIT License'],
               keywords='move, files, interactive',
               py_modules=['move'],
               scripts=['move', 'qmv-move-helper'])
