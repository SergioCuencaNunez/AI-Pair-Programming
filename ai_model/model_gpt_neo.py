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
            input_ids = torch.LongTensor(tokenizer.encode(problem.get_prompt(), verbose=False)).unsqueeze(0)  
            output_ids = model.generate(input_ids,num_beams=5,early_stopping=True,max_length=1024 - len(input_ids))
            output_str = tokenizer.decode(output_ids[0])
            solutions.add_problem_solution(problem_id, output_str)