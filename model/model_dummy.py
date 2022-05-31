class Model:
    def __init__(self, conf):
        self._conf = conf
    
    def apply_model(self, problems):
        for problem in problems:
            model = problem.get_prompt()
            return model