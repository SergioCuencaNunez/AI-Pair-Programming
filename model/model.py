class Model:
    def __init__(self, function):
        self._function = function
    
    def get_function(self):
        return self._function

model = Model("def return_x(x):\n  return x")
print(model.get_function())