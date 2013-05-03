====
move
====

Interactively moves files under revision control using a text editor.

.. image:: https://raw.github.com/myint/move/master/screenshot1.png
   :alt: screenshot
   :align: center

.. image:: https://raw.github.com/myint/move/master/screenshot2.png
   :alt: screenshot
   :align: center

.. image:: https://raw.github.com/myint/move/master/screenshot3.png
   :alt: screenshot
   :align: center


Installation
============

*move* depends on *renameutils*.

Under MacPorts::

   $ sudo port install renameutils

Under Ubuntu::

   $ sudo apt-get install renameutils

To install *move*::

   $ pip install move


Features
========

*move* supports multiple revision control systems. It tries them in order:

- ``git mv``
- ``svn mv``
- ``hg mv``

If above commands all fail, it falls back to running plain ``mv``.
