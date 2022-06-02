from ai_results.results import Results
from ai_results.result import Result

class Results_Dummy(Results):
    def __init__(self):
        super().__init__()

    def add_problem_result(self, problem_id, result):
        if problem_id not in self.results:
            self.results[problem_id] = []

        self.results[problem_id].append(Result(result))

    def get_problem_results(self, problem_id):
        return self.results[problem_id]