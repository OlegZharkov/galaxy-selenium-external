#!/bin/bash
# Prepare
sudo apt-get update && sudo apt-get install python3-venv -y
python -m venv galaxy/.venv

source "galaxy/.venv/bin/activate" # activate virtualenv
pip install -r galaxy/lib/galaxy/dependencies/dev-requirements.txt && pip install -r galaxy/requirements.txt
python test_parser.py
