import sys,os
import torch
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_model.model import Model

class Model_GPT_Neo(Model):
    def __init__(self, conf=None):
        super().__init__(conf)

    def apply_model(self, problems, solutions):
        from transformers import pipeline, AutoConfig
        config = AutoConfig.from_pretrained('/local/config.json')
        #model = torch.load(r"/local/pytorch_model.bin", map_location=torch.device('cpu'), config=config)
        model = torch.hub.load(r'/local/pytorch_model.bin', 'model', from_tf=True, config=config)

        #model.eval()
        #generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
        generator = pipeline('text-generation', model = model)
        for problem_id, problem in problems.get_problems().items():
            solution_array = generator(problem.get_prompt(), do_sample=True, max_length=200)
            solutions.add_problem_solution(problem_id, solution_array[0]['generated_text'])