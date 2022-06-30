import sys,os
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_unit_testing.unit_tests import Unit_Tests
from ai_unit_testing.unit_test_dummy import Unit_Test_Dummy
#from ai_unit_testing.unit_test_gpt_neo import Unit_Test_GPT_Neo
#from ai_unit_testing.unit_test_codegpt import Unit_Test_CodeGPT
#from ai_unit_testing.unit_test_sql import Unit_Test_SQL

class Unit_Tests_Dummy(Unit_Tests):
    def __init__(self, path):
        super().__init__(path)
    
    def read_tests(self):
        self.tests = {}
       
        with open(self.path, 'r') as json_file:
            tests_json = list(json_file)
        
        for test_json in tests_json:
            test = json.loads(test_json)
            self.tests[test['test_id']] = Unit_Test_Dummy(test['test_id'], test['test'])

        return self.tests

    def get_problem_test(self, problem_id):
        return self.tests[problem_id]

    def apply_unit_tests(self, problems, solutions, results):
        for problem_id, problem in problems.get_problems().items():
            unit_test = self.get_problem_test(problem_id)

            for solution in solutions.get_problem_solutions(problem_id):
                result = unit_test.apply_test(problem, solution)
                results.add_problem_result(problem_id, result)
