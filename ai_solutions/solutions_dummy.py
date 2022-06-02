from ai_solutions.solutions import Solutions
from ai_solutions.solution import Solution

class Solutions_Dummy(Solutions):
    def __init__(self):
        super().__init__()
        self.solutions = {}

    def add_problem_solution(self, problem_id, solution_code):
        if problem_id not in self.solutions:
            self.solutions[problem_id] = []

        self.solutions[problem_id].append(Solution(solution_code))

    def get_problem_solutions(self, problem_id):
        return self.solutions[problem_id]