import sys,os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_GPT_Neo(Model):
    def __init__(self, conf=None):
        super().__init__(conf)

    def apply_model(self, problems, solutions):
        from transformers import pipeline
        #generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
        generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')
        for problem_id, problem in problems.get_problems().items():
            solution_array = generator(problem.get_prompt(), do_sample=True, max_length=200)
            solutions.add_problem_solution(problem_id, solution_array[0]['generated_text'])