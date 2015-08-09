#!/bin/bash -eux

rm -rf ./.test
mkdir -p ./.test/1
EDITOR=./fake move ./.test
ls ./.test/2
rm -rf ./.test
