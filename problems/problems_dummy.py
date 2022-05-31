import json
import problem as pb
from problems import Problems

class Problems_Dummy(Problems):
    def __init__(self, path):
        super().__init__(path)

    def get_problems(self):
        self._problems = [] 
       
        with open(self._path, 'r') as json_file:
            problems_json = list(json_file)
        
        for problem_json in problems_json:
            problem = json.loads(problem_json)
            problem_class = pb.Problem(problem['task_id'],problem['prompt'],problem['canonical_solution'],problem['entry_point'])
            self._problems.append(problem_class)
        return self._problems
    
problems = Problems_Dummy('./data/problems.jsonl')