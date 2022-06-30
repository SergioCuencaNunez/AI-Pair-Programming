import sys,os
import openai
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_Codex(Model):
    def __init__(self, conf=None):
        super().__init__(conf)

    def apply_model(self, problems, solutions):
        openai.api_key = "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"
        for problem_id, problem in problems.get_problems().items():
            response = openai.Completion.create(
                engine = "code-davinci-002",
                prompt = problem.get_question() + problem.get_prompt(),
                temperature = 0,
                max_tokens = 1500,
                top_p = 1,
                frequency_penalty = 0,
                presence_penalty = 0)
            #print(response['choices'][0]['text'])
            #for x in response['choices'][0]['text']:
             #   print(x)
            solutions.add_problem_solution(problem_id, response['choices'][0]['text'])
