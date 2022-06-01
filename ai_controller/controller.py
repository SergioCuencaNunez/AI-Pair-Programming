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
        programs = {}
        for i, problem in enumerate(self.problems):
            check_program = (
                self.problems[problem]["prompt"] + self.solutions[problem]["solution"] + "\n" +
                self.tests[problem]["test"] + "\n" +
                f"check({self.problems[problem]['entry_point']})" + "\n"
            )
            programs[self.problems[problem]["task_id"]] = check_program
        return programs

controller = Controller()
programs = controller.apply_unit_tests()
print(programs)