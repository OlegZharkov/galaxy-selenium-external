#!/bin/bash
# Prepare
python -m venv galaxy/.venv

source "galaxy/.venv/bin/activate" # activate virtualenv
pip install -r galaxy/lib/galaxy/dependencies/dev-requirements.txt -r galaxy/requirements.txt  &> /dev/null
python test_parser.py $1