from abc import abstractmethod

class Problems:
    def __init__(self, path):
        self.path = path
        self.problems = self.read_problems()

    def get_problems(self):
        return self.problems

    @abstractmethod
    def read_problems(self):
        raise NotImplementedError()