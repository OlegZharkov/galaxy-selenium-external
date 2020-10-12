#!/bin/bash
git clone https://github.com/galaxyproject/galaxy.git --branch release_20.09 --single-branch ./dist && cd dist/
GALAXY_TEST_EXTERNAL=http://usegalaxy.eu/ ./run_tests.sh -selenium lib/galaxy_test/selenium/test_tool_form.py:ToolFormTestCase.test_verify_dataset_details_tables