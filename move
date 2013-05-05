#!/usr/bin/env python

"""Main script."""

import sys

import move

try:
    move.interactive_move(sys.argv[1:])
except OSError:
    raise SystemExit('"qmv" binary not found; it is from "renameutils"')
except KeyboardInterrupt:
    sys.exit(1)
