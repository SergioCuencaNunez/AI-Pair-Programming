import sys,os
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_problems.problem import Problem
from ai_problems.problems import Problems

class Problems_Dummy(Problems):
    def __init__(self, path):
        super().__init__(path)

    def read_problems(self):
        problems = {}
       
        with open(self.path, 'r') as json_file:
            problems_json = json_file.readlines()
        
        for problem_json in problems_json:
            problem = json.loads(problem_json)
            problems[problem['task_id']] = Problem(problem['task_id'], problem['prompt'], problem['canonical_solution'], problem['entry_point'])

        return problems
