#!/usr/bin/env python
# Copyright (C) 2021 The uecho-py Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

.PHONY: clean format build uninstall upload doc test

all: test

clean:
	rm -rf tests/__pycache__
	rm -rf tests/*/__pycache__

format:
	yapf -ir --style setup.cfg uecho bin test examples

lint: format
	flake8 uecho bin test examples
	# find uecho -name "*.py" | xargs pylint 

type: format
	mypy uecho

test: 
	env PYTHONPATH=`pwd` py.test -v test

build:
	rm -rf dist
	python3 -m build

install: build
	pip install `ls -1 dist/*.tar.gz`

uninstall:
	pip uninstall -y uecho

upload: build
	python3 -m twine upload dist/*

doc:
	pip install sphinx-rtd-theme
	mkdir -p ./doc/build
	sphinx-apidoc -f -o ./doc/conf uecho
	sphinx-build -b html ./doc/conf ./doc/build
