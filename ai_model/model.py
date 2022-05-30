import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_problems.problems import problems

class Model:
    def __init__(self, conf):
        self._conf = conf
    
    def apply_model(self):
        for problem in problems:
            model = problem.get_prompt()
            return model

model = Model("def return_x(x):\n  return x")
print(model.apply_model())