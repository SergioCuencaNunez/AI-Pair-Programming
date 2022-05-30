import problem as pb
import json

class Problems:
    def __init__(self, problems = []):
        self._problems = problems

    def get_problems(self):
        with open('./data/problems.jsonl', 'r') as json_file:
            problems_json = list(json_file)

        self._problems = []
        for problem_json in problems_json:
            problem = json.loads(problem_json)
            problem_class = pb.Problem(problem['task_id'],problem['prompt'],problem['canonical_solution'],problem['entry_point'])
            self._problems.append(problem_class)
        
        return self._problems
