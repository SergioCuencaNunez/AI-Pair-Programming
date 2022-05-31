import json
import unit_test as ut

class Unit_Tests:
    def __init__(self, path):
        self._path = path
        self._tests = self.get_tests()
    
    def get_tests(self):
        self._tests = [] 
       
        with open(self._path, 'r') as json_file:
            tests_json = list(json_file)
        
        for test_json in tests_json:
            test = json.loads(test_json)
            test_class = ut.Unit_Test(test['test_id'],test['test'])
            self._tests.append(test_class)
        return self._tests

tests = Unit_Tests('./data/tests.jsonl')