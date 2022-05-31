import json
import unit_test as ut
from unit_tests import Unit_Tests

class Unit_Tests_Dummy(Unit_Tests):
    def __init__(self, path):
        super().__init__(path)
    
    def get_tests(self):
        self._tests = [] 
       
        with open(self._path, 'r') as json_file:
            tests_json = list(json_file)
        
        for test_json in tests_json:
            test = json.loads(test_json)
            test_class = ut.Unit_Test(test['test_id'],test['test'])
            self._tests.append(test_class)
        return self._tests

tests = Unit_Tests_Dummy('./data/tests.jsonl')