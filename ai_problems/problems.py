from abc import abstractmethod

class Problems:
    def __init__(self, path):
        self.path = path
        self.problems = self.get_problems()

    @abstractmethod
    def get_problems(self):
        raise NotImplementedError()