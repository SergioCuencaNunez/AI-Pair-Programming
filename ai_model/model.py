from abc import abstractmethod

class Model:
    def __init__(self, conf = None):
        self.conf = conf
    
    @abstractmethod
    def apply_model(self, problems, solutions):
        raise NotImplementedError()