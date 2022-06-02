class Results:
    def __init__(self):
        self.results = {}

    def get_results(self):
        return self.results

    def add_problem_result(self, problem_id, result):
        raise NotImplementedError()

    def get_problem_results(self, problem_id):
        raise NotImplementedError()