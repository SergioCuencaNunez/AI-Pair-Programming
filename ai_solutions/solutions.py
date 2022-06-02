from abc import abstractmethod

class Solutions:
    def __init__(self):
        self.solutions = {}

    def get_solutions(self):
        return self.solutions

    @abstractmethod
    def add_problem_solution(self, problem_id, solution_code):
        raise NotImplementedError()

    @abstractmethod
    def get_problem_solutions(self, problem_id):
        raise NotImplementedError()
