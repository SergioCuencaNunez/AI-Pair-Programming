import sys,os
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_unit_testing.unit_test import Unit_Test
from ai_unit_testing.unit_tests import Unit_Tests

class Unit_Tests_Dummy(Unit_Tests):
    def __init__(self, path):
        super().__init__(path)
    
    def get_tests(self):
        self.tests = {} 
       
        with open(self.path, 'r') as json_file:
            tests_json = list(json_file)
        
        for test_json in tests_json:
            test = json.loads(test_json)
            test_class = Unit_Test(test['test_id'],test['test'])
            self.tests[test['test_id']] = test_class.__dict__
        return self.tests
    
    #def apply_unit_tests(self, programs):
    #    unit_tests = {}
    #    for i, program in enumerate(programs):
