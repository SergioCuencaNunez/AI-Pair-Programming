import sys,os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_CodeGPT(Model):
    def __init__(self, conf=None):
        super().__init__(conf)

    def apply_model(self, problems, solutions):
        from transformers import pipeline, set_seed
        set_seed(42)
        generator = pipeline('text-generation', model='microsoft/CodeGPT-small-py')
        for problem_id, problem in problems.get_problems().items():
            solution_array = generator(problem.get_prompt(), max_length=300, num_return_sequences=1)
            solutions.add_problem_solution(problem_id, solution_array[0]['generated_text'])