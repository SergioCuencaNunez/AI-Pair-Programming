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
                temperature = 0,
                max_tokens = 275,
                top_p = 1,
                n = 10,
                frequency_penalty = 0,
                presence_penalty = 0)
            for x in response['choices']:
                solutions.add_problem_solution(problem_id, self._clean_solution(x['text']))
     
    def _clean_solution(self, solution):
        new_solution = ''
        count = 0
        for line in solution.splitlines(True):
            if line.startswith('#') or line.startswith('-') or line.startswith('`') or line.startswith('<') or line.startswith('>') or line.startswith('/') or line.startswith('http') or line.startswith('"') or line.startswith('$') or line.startswith('+') or line.startswith('!') or line.startswith('@') or line[0].isupper():
                continue 
            if re.match("^(def|class) .*", line):
                count += 1   
                if count == 2:
                    break
            if re.match("^[^\r\n\t\f\v\# ]", line):
                if count > 1:
                    break
            new_solution += line
            
        return new_solution