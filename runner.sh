#!/bin/bash
git clone https://github.com/galaxyproject/galaxy.git --branch release_20.09 --single-branch ./dist && cd dist/
#GALAXY_TEST_EXTERNAL=https://usegalaxy.org/ ./run_tests.sh -selenium lib/galaxy_test/selenium/test_history_multi_view.py:HistoryMultiViewTestCase.test_create_new_old_slides_next
#GALAXY_TEST_EXTERNAL=https://usegalaxy.eu/ ./run_tests.sh -selenium lib/galaxy_test/selenium/test_uploads.py:UploadsTestCase.test_upload_simplest
GALAXY_TEST_EXTERNAL=https://usegalaxy.eu/ ./run_tests.sh -selenium lib/galaxy_test/selenium/test_navigates_galaxy.py:NavigatesGalaxySeleniumTestCase.test_click_error