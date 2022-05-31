from model import Model

class Model_Dummy(Model):
    def __init__(self, conf):
        super().__init__(conf)
    
    def apply_model(self, problems):
        for problem in problems:
            model = problem.get_prompt()
            return model