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
    
    def get_problems(self):
        data = Problems_Dummy('./ai_data/problems.jsonl').__dict__
        return data['problems']

    def apply_model(self):
         return Model_Dummy.apply_model(self, self.problems)
    
    #def apply_unit_testing(self):


controller = Controller()
solutions = controller.get_problems()
print(solutions)