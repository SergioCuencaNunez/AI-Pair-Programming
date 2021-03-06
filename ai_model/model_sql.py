import sys,os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_SQL(Model):
    def __init__(self, conf=None):
        super().__init__(conf)
    
    def apply_model(self, problems, solutions):
        for problem_id, problem in problems.get_problems().items():
            # Llamada al modelo
            solution = problem.get_canonical_solution()
            solutions.add_problem_solution(problem_id, solution)