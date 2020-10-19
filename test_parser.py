import ast
import sys
from os import listdir
from os.path import isfile, join
import pytest
from io import StringIO
from os import environ
import requests
import sys
import json

galaxy_root_dir = "galaxy/"
selenium_test_dir = "lib/galaxy_test/selenium/"

test_root_dir = galaxy_root_dir + selenium_test_dir


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
            test_name = f'{parts[1]}.{parts[2]}'
            test_path = f'{parts[0]}:{test_name}'

            current_available_tests.append(test_path)

    return current_available_tests


test_files = [f for f in listdir(test_root_dir) if isfile(join(test_root_dir, f)) and f.startswith("test_")]

selenium_tests = []
for test_file in test_files:
    path = test_root_dir + test_file
    if not is_admin(path):
        selenium_tests += get_individual_tests(path)
print(json.dumps(selenium_tests).replace('"', '\\"'))

# for test_name, test_path in selenium_tests:
#     raw_data = """{
#      "event_type": "%s",
#       "client_payload": {
#         "galaxy_selenium_test_path": "%s"
#       }
#     }""" % (test_name, test_path)
#
#     # Auth token as an argument
#     requests.post(url="https://api.github.com/repos/OlegZharkov/galaxy-selenium-external/dispatches",
#                       headers={"Authorization": "token %s" % sys.argv[1]},
#                       data=raw_data
#                       )
