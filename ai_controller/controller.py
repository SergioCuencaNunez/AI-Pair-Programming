import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_problems.problems_dummy import Problems_Dummy
from ai_model.model_dummy import Model_Dummy
from ai_unit_testing.unit_tests_dummy import Unit_Tests_Dummy

class Controller:
    def __init__(self):
        self.problems = self.get_problems()
        self.solutions = self.apply_model()
        self.tests = self.get_tests()
    
    def get_problems(self):
        data = Problems_Dummy('./ai_data/problems.jsonl').__dict__
        return data['problems']

    def apply_model(self):
         return Model_Dummy.apply_model(self, self.problems)
    
    def get_tests(self):
        data = Unit_Tests_Dummy('./ai_data/tests.jsonl').__dict__
        return data['tests']

    def apply_unit_tests(self):
        solutions = {}
        for i, solution in self.solutions.items():
            completion = (solution["solution"]
            )
            solutions[i] = completion

        tests = {}
        for i, test in self.tests.items():
            test = (test["test"]
            )
            tests[i] = test

        programs = {}
        for i, problem in self.problems.items():
            check_program = (
                problem["prompt"] + solutions[i] + "\n" +
                tests[i] + "\n" +
                f"check({problem['entry_point']})" + "\n"
            )
            programs[i] = check_program
        
        return Unit_Tests_Dummy.apply_unit_tests(self, programs, self.tests)