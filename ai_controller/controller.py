import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_problems.problems_dummy import Problems_Dummy
from ai_model.model_dummy import Model_Dummy
from ai_unit_testing.unit_tests_dummy import Unit_Tests_Dummy
from ai_solutions.solutions_dummy import Solutions_Dummy
from ai_results.results_dummy import Results_Dummy


class Controller:
    def __init__(self):
        self.problems = Problems_Dummy('./ai_data/problems.jsonl')
        self.model = Model_Dummy()
        self.unit_tests = Unit_Tests_Dummy('./ai_data/tests.jsonl')
        self.solutions = Solutions_Dummy()
        self.results = Results_Dummy()

        self.model.apply_model(self.problems, self.solutions)
        self.unit_tests.apply_unit_tests(self.problems, self.solutions, self.results)


c = Controller()

print(c.problems.get_problems())
print(c.unit_tests.get_tests())
print(c.solutions.get_solutions())
print(c.results.get_results())
