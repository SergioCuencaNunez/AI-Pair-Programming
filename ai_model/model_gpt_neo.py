import sys,os
import torch
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_GPT_Neo(Model):
    def __init__(self, conf=None):
        super().__init__(conf)

    def apply_model(self, problems, solutions):
        from transformers import GPTNeoConfig, GPTNeoForCausalLM, GPT2Tokenizer 
        config = GPTNeoConfig.from_pretrained('/local/weights_apps/config.json')
        model = GPTNeoForCausalLM.from_pretrained('/local/weights_apps/pytorch_model.bin', config=config)
        tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
        for problem_id, problem in problems.get_problems().items():
            input = "\nQUESTION:\n" + problem.get_question() + "\n" + problem.get_prompt() + "\n" + "\nUse Call-Based Format\n\nANSWER:\n"
            input_ids = torch.LongTensor(tokenizer.encode(input, verbose=False)).unsqueeze(0)  
            for i in range(10):
                output_ids = model.generate(input_ids, num_beams = 1, early_stopping = True, max_length = 1024 - len(input_ids), do_sample = True, temperature = 0.6)
                output_str = tokenizer.decode(output_ids[0])
                solutions.add_problem_solution(problem_id, self._clean_solution(output_str))
       
    def _clean_solution(self, solution):
        new_solution = ''
        count = 0
        solution_cropped, head, tail = solution.partition("ANSWER:\n")
        for line in solution_cropped.splitlines(True):
            if line.startswith('#') or line.startswith('-') or line.startswith('`') or line.startswith('<') or line.startswith('>') or line.startswith('/') or line.startswith('http') or line.startswith('"') or line[0].isupper():
                continue 
            if re.match("^(def|class) .*", line):
                count += 1
                if count == 2:
                    break
            new_solution += line
            
        return new_solution