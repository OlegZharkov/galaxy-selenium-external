#!/bin/bash
# Prepare
python -m venv galaxy/.venv

source "galaxy/.venv/bin/activate" # activate virtualenv
pip install -r galaxy/lib/galaxy/dependencies/dev-requirements.txt && pip install -r galaxy/requirements.txt
python test_parser.py

curl --location --request POST --url 'https://api.github.com/repos/OlegZharkov/galaxy-selenium-external/dispatches' --header 'Authorization: token ${{ secrets.GITHUB_TOKEN }}' --header 'Accept: application/vnd.github.everest-preview+json' --header 'Content-Type: application/json' --data-raw '{
  "event_type": "test-repository-dispatch",
  "client_payload": {
    "unit": false,
    "integration": true
  }
}'