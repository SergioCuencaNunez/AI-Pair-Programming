import problem as pb
import json

def get_data():
    with open('./data/problems.jsonl', 'r') as json_file:
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
            problem_class = pb.Problem(problem['task_id'],problem['prompt'],problem['canonical_solution'],problem['entry_point'])
            self._problems.append(problem_class)
        
        return self._problems

problemas = Problems(get_data()).get_problems()