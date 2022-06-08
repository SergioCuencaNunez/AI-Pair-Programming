from distutils.sysconfig import get_makefile_filename
import sys,os
import pandas as pd
import openpyxl as xl
import random as rm
from sklearn import metrics

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from ai_controller.controller import Controller

class Metrics:
    def __init__(self):
        self.problems = Controller().problems.get_problems()
        self.solutions = Controller().solutions.get_solutions()
        self.results = Controller().results.get_results()
        self.metrics = self.get_metrics()

    def get_metrics(self):
        metrics = []

        for problem_id, problem in self.problems.items(): 
            metrics.append(problem.__dict__)
        
        for problem_id, solutions in self.solutions.items(): 
            problem_solutions = []
            for solution in solutions:
                solution = solution.get_solution()
                problem_solutions.append(solution)
            self.solutions.update({problem_id : problem_solutions})
        
        for problem_id, results in self.results.items(): 
            problem_results = []
            for result in results:
                result = result.get_result()
                problem_results.append(result)
            self.results.update({problem_id : problem_results})

        for problem in metrics:
            for problem_id, solutions in self.solutions.items(): 
                if problem_id == problem["task_id"]:
                    problem.update({"canonical_solution" : self.solutions[problem_id]})
                    problem["solutions"] = problem.pop("canonical_solution")
                    problem["result"] = self.results[problem_id]
    
        return metrics 

    def export_metrics(self):
        df = pd.DataFrame.from_dict(self.metrics)
        df.to_excel("metrics.xlsx")
        wb = xl.load_workbook('./metrics.xlsx')
        ws = wb.active
        ws.delete_cols(idx = 1)
        wb.save('./metrics.xlsx')
    
    def import_metrics(self):
        df = pd.read_excel(r'./metrics.xlsx')
        metrics = df.to_dict('records')
        return metrics
    
    def pass_at_k(self):
        for i in [1,5,10]: 
            for problem in self.metrics:
                if i == 1:
                    if rm.choice(problem["result"]):
                        problem["pass@" + str(i)] = "OK"
                    else:
                        problem["pass@" + str(i)] = "KO"
                elif i == 5:
                    if any(rm.sample(problem["result"], 5)):
                        problem["pass@" + str(i)] = "OK"
                    else:
                        problem["pass@" + str(i)] = "KO"
                else:
                    if any(problem["result"]):
                        problem["pass@" + str(i)] = "OK"
                    else:
                        problem["pass@" + str(i)] = "KO"
        
        self.export_metrics()

m = Metrics()
m.export_metrics()
