class Problem:
    def __init__(self, task_id, prompt, canonical_solution, entry_point):
        self._task_id = task_id
        self._prompt = prompt
        self._canonical_solution = canonical_solution
        self._entry_point = entry_point
    
    def get_task_id(self):
        return self._task_id

    def get_prompt(self):
        return self._prompt

    def get_canonical_solution(self):
        return self._canonical_solution

    def get_entry_point(self):
        return self._entry_point
    
    def set_task_id(self, value):
        self._task_id = value

    def set_prompt(self, value):
        self._prompt = value
    
    def set_canonical_solution(self, value):
        self._canonical_solution = value
    
    def set_entry_point(self, value):
        self._entry_point = value
    

problem = Problem("test/0", "def return_x(x):\n", "return x", "return_x(x)")