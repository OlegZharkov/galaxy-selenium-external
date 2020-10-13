#!/bin/bash
git clone https://github.com/galaxyproject/galaxy.git --branch release_20.09 --single-branch ./dist && cd dist/
GALAXY_TEST_EXTERNAL=https://usegalaxy.org/ ./run_tests.sh -selenium lib/galaxy_test/selenium/test_history_multi_view.py:HistoryMultiViewTestCase.test_create_new_old_slides_next
