import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_problems.problems_dummy import Problems_Dummy
#from ai_model.model_codex import Model_Codex
from ai_model.model_gpt_neo import Model_GPT_Neo
#from ai_model.model_codegpt import Model_CodeGPT
#from ai_model.model_sql import Model_SQL
from ai_unit_testing.unit_tests_dummy import Unit_Tests_Dummy
from ai_solutions.solutions_dummy import Solutions_Dummy
from ai_results.results_dummy import Results_Dummy
from ai_metrics.metrics import Metrics

class Controller:
    def __init__(self):
        self.problems = Problems_Dummy('./ai_data/problems_test.jsonl')
        self.model = Model_GPT_Neo()
        self.unit_tests = Unit_Tests_Dummy('./ai_data/tests_test.jsonl')
        self.solutions = Solutions_Dummy()
        self.results = Results_Dummy()
        self.metrics = Metrics('./metrics_gpt_neo.xlsx')

        self.model.apply_model(self.problems, self.solutions)
        self.unit_tests.apply_unit_tests(self.problems, self.solutions, self.results)
        self.metrics.get_metrics(self.problems, self.solutions, self.results)

c = Controller()
print(c.metrics.export_metrics())