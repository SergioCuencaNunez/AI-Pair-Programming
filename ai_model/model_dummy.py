import sys,os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_Dummy(Model):
    def __init__(self, conf="from transformers import pipeline, set_seed"):
        super().__init__(conf)

    def apply_model(self, problems, solutions):
        for problem_id, problem in problems.get_problems().items():
            generator = pipeline('text-generation', model='microsoft/CodeGPT-small-py')
            solution = generator(problem.get_prompt(), max_length=200, num_return_sequences=5)
            print(solution)
            solutions.add_problem_solution(problem_id, solution)