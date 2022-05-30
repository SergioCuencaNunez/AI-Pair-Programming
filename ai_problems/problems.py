import sys,os
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_problems.problem import Problem as pb

def get_data():
    with open('./ai_data/problems.jsonl', 'r') as json_file:
            problems_json = list(json_file)
    return problems_json

class Problems:
    def __init__(self, problems = []):
        self._problems = problems

    def get_problems(self):
        problems_json = get_data()
        self._problems = [] 
        for problem_json in problems_json:
            problem = json.loads(problem_json)
            problem_class = pb(problem['task_id'],problem['prompt'],problem['canonical_solution'],problem['entry_point'])
            self._problems.append(problem_class)
        
        return self._problems

problems = Problems(get_data()).get_problems()