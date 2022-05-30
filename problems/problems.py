import problem as pb
import json

class Problems:
    def __init__(self, problem):
        self._problem = problem

    def get_problem(self):
        return self._problem

    def get_problems(self):
        with open('./data/problems.jsonl', 'r') as json_file:
            problems_json = list(json_file)

        problems = []

        for problem_json in problems_json:
            problem = json.loads(problem_json)
            problem_class = pb.Problem(problem['task_id'],problem['prompt'],problem['canonical_solution'],problem['entry_point'])
            problems.append(problem_class)
        
        return problems
