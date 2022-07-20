import sys, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_CodeGPT(Model):
    def __init__(self, conf=None):
        super().__init__(conf)

    def apply_model(self, problems, solutions):
        from transformers import pipeline, set_seed
        set_seed(42)
        generator = pipeline('text-generation', model='microsoft/CodeGPT-small-py')
        for problem_id, problem in problems.get_problems().items():
            for i in range(10):
                solution_array = generator(problem.get_question() + problem.get_prompt(), max_length=200, num_return_sequences = 1, do_sample = True)
                solutions.add_problem_solution(problem_id, solution_array[0]['generated_text'])
    
    
    def _clean_solution(self, solution):
        new_solution = ''
        count = 0
        for line in solution.splitlines(True):
            if line.startswith('#') or line.startswith('-') or line.startswith('`') or line.startswith('<') or line.startswith('>') or line.startswith('/') or line.startswith('http') or line.startswith('"') or line.startswith('$') or line[0].isupper():
                continue 
            if re.match("^(def|class) .*", line):
                count += 1   
                if count == 2:
                    break
            if re.match("^[^\r\n\t\f\v\# ]", line):
                break
            new_solution += line
            
        return new_solution