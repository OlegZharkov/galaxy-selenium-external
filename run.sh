#!/bin/bash
# Prepare
python -m venv
. galaxy/.venv/bin/activate
pip install pytest
pip install -r galaxy/requirements.txt

# Run
python test_parser.py