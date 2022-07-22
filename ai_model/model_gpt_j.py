import sys, os, re, json
import requests
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_GPT_J(Model):
    def __init__(self, conf=None):
        super().__init__(conf)
    
    def apply_model(self, problems, solutions):        
        url = 'https://api.eleuther.ai/completion'
        for problem_id, problem in problems.get_problems().items():
            body = {"context": problem.get_question() + "\n" + problem.get_prompt(),"top_p":1,"temp":0,"response_length":400,"remove_input":True}
            for i in range(30):
                r = requests.post(url, json = body)
                data = r.json()
                solutions.add_problem_solution(problem_id, self._clean_solution(data[0]["generated_text"]))
    
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