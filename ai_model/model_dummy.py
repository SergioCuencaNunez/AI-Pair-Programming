import sys,os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_Dummy(Model):
    def __init__(self, conf):
        super().__init__(conf)
    
    def apply_model(self, problems):
        solutions = {}
        for problem in problems:
            prompt_solution = {}
            prompt_solution["solution"] = problems[problem]['prompt'] + problems[problem]['canonical_solution']
            solutions[problem] = prompt_solution
        return solutions