from abc import abstractmethod

class Unit_Tests:
    def __init__(self, path):
        self._path = path
        self._tests = self.get_tests()
    
    @abstractmethod
    def get_tests(self):
        raise NotImplementedError()
