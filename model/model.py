class Model:
    def __init__(self, conf):
        self._conf = conf
    
    def apply_model(self):
        #return self._function

model = Model("def return_x(x):\n  return x")
