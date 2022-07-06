import sys, os, re
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
                temperature = 0.6,
                max_tokens = 1500,
                top_p = 0.95,
                n = 10,
                frequency_penalty = 0,
                presence_penalty = 0)
            #print(response['choices'][0]['text'])
            for x in response['choices']:
                #solutions.add_problem_solution(problem_id, re.split(r"^\n", x['text'])[0])
                solutions.add_problem_solution(problem_id, self._clean_solution(x['text']))
     
    def _clean_solution(self, solution):
        new_solution = ''
        count = 0
        for line in solution.splitlines(True):
            if line.startswith('#') or line.startswith('-') or line.startswith('`') or line.startswith('<') or line.startswith('>') or line.startswith('/') or line.startswith('http') or line.startswith('"') or line[0].isupper():
                continue 
            if re.match("^(def|class) .*", line):
                count += 1
                if count == 2:
                    break
            new_solution += line
            
        return new_solution