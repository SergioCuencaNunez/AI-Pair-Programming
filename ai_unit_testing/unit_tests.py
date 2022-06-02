from abc import abstractmethod

class Unit_Tests:
    def __init__(self, path):
        self.path = path
        self.tests = {}

        self.read_tests()

    def get_tests(self):
        return self.tests

    @abstractmethod
    def read_tests(self):
        raise NotImplementedError()

    @abstractmethod
    def get_problem_test(self, problem_id):
        raise NotImplementedError()

    @abstractmethod
    def apply_unit_tests(self, problems, solutions, results):
        raise NotImplementedError()