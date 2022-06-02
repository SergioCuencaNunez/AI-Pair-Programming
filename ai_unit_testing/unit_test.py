class Unit_Test:
    def __init__(self, problem_id, test):
        self.problem_id = problem_id
        self.test = test
        self.result = None

    def get_problem_id(self):
        return self.problem_id

    def get_test(self):
        return self.test
    
    def set_test_problem_id(self, value):
        self.problem_id = value
    
    def set_test(self, value):
        self.test = value

    def apply_test(self, problem, solution):
        raise NotImplementedError()

    def _execute_test(self, program):
        raise NotImplementedError()
