class Problem:
    def __init__(self, task_id, question, prompt, canonical_solution, entry_point):
        self.task_id = task_id
        self.question = question
        self.prompt = prompt
        self.canonical_solution = canonical_solution
        self.entry_point = entry_point

    def get_task_id(self):
        return self.task_id

    def get_question(self):
        return self.question
    
    def get_prompt(self):
        return self.prompt

    def get_canonical_solution(self):
        return self.canonical_solution

    def get_entry_point(self):
        return self.entry_point
    
    def set_task_id(self, value):
        self.task_id = value

    def set_question(self, value):
        self.question = value

    def set_prompt(self, value):
        self.prompt = value
    
    def set_canonical_solution(self, value):
        self.canonical_solution = value
    
    def set_entry_point(self, value):
        self.entry_point = value