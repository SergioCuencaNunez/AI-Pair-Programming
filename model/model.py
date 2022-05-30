class Model:
    def __init__(self, conf):
        self._conf = conf
    
    def apply_model(self):
        for problem in problemas:
            model = problem['prompt']
            return model

model = Model("def return_x(x):\n  return x")
