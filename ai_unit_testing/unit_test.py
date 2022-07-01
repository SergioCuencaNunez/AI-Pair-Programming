class Unit_Test:
    def __init__(self, problem_id, file, function):
        self.problem_id = problem_id
        self.file = file
        self.function = function
        self.result = None

    def get_problem_id(self):
        return self.problem_id

    def get_file(self):
        return self.file
    
    def get_function(self):
        return self.function
    
    def set_test_problem_id(self, value):
        self.problem_id = value
    
    def set_file(self, value):
        self.file = value
    
    def set_function(self, value):
        self.function = value

    def apply_test(self, problem, solution):
        raise NotImplementedError()

    def _execute_test(self, program):
        raise NotImplementedError()
