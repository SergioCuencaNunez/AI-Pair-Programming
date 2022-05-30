import sys,os
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_unit_testing.unit_test import Unit_Test as ut

def get_data():
    with open('./ai_data/tests.jsonl', 'r') as json_file:
            tests_json = list(json_file)
    return tests_json

class Unit_Tests:
    def __init__(self, tests = []):
        self._tests = tests

    def get_tests(self):
        tests_json = get_data()
        self._problems = [] 
        for test_json in tests_json:
            test = json.loads(test_json)
            test_class = ut(test['test_id'],test['test'])
            print(test_class)
            self._tests.append(test_class)
        
        return self._tests

problems = Unit_Tests(get_data()).get_tests()