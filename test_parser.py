import ast
import sys
from os import listdir
from os.path import isfile, join
import pytest
from io import StringIO
from io import environ
import requests

galaxy_root_dir = "galaxy/"
selenium_test_dir = "lib/galaxy_test/selenium/"

test_dir_path = galaxy_root_dir + selenium_test_dir


# https://stackoverflow.com/a/44699395/4870846
def is_admin(filename):
    with open(filename) as file:
        node = ast.parse(file.read())

    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
    for class_ in classes:
        asssings = [n for n in class_.body if isinstance(n, ast.Assign)]
        for var in asssings:
            for target in var.targets:
                if target.id == "requires_admin" and var.value.value == True:
                    return True
        return False


def get_individual_tests(test_file_path):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    pytest.main(["--co", "-q", "--disable-pytest-warnings", test_file_path])

    sys.stdout = old_stdout

    current_available_tests = []
    for line in mystdout.getvalue().splitlines():
        if selenium_test_dir in line:
            parts = line.split("::")
            current_available_tests.append(f'{parts[0]}:{parts[1]}.{parts[2]}')

    return current_available_tests


test_files = [f for f in listdir(test_dir_path) if isfile(join(test_dir_path, f)) and f.startswith("test_")]

selenium_tests = []
for test_file in test_files:
    selenium_tests += get_individual_tests(test_dir_path + test_file)



for selenium_test_path in selenium_tests:
    raw_data = """{
     "event_type": "test-repository-dispatch",
      "client_payload": {
        "galaxy_selenium_test_path": "%s"
      }
    }""" % selenium_test_path
    x = requests.post(url="https://api.github.com/repos/OlegZharkov/galaxy-selenium-external/dispatches",
                  headers={"Authorization": "token %s" % environ['API_KEY']},
                  data=raw_data
                  )
