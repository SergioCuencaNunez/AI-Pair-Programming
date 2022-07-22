import pandas as pd
import openpyxl as xl
import random as rm

class Metrics:
    def __init__(self, path):
        self.path = path
        self.metrics = {}

    def get_metrics(self, problems, solutions, results):
        metrics_list = self.write_metrics(problems, solutions, results)
        
        for problem in metrics_list:
            self.metrics[problem["task_id"]] = problem
        
        self.pass_at_k()

        return self.metrics

    def write_metrics(self, problems, solutions, results):
        metrics_list = []

        for problem_id, problem in problems.get_problems().items():
            metrics_list.append(problem.__dict__)
        
        for problem in metrics_list:
            #Intentar optimizar para no recorrer todas las soluciones
            for problem_id, problem_solutions in solutions.get_solutions().items(): 
                if problem_id == problem["task_id"]:             
                    problem["solutions"] =  list(map(lambda solution: solution.get_solution(), solutions.get_problem_solutions(problem_id)))
                    problem["result"] =  list(map(lambda result: result.get_result(), results.get_problem_results(problem_id)))
                    #problem.pop("entry_point")

        return metrics_list
    
    def pass_at_k(self):
        for i in [1,10,30]:
            for problem_id, problem in self.metrics.items():
                if any(rm.sample(problem["result"], i)):
                    problem["pass@" + str(i)] = "OK"
                else:
                    problem["pass@" + str(i)] = "KO"
    
    def export_metrics(self):
        df = pd.DataFrame.from_dict(self.metrics, orient='index')
        df.to_excel(self.path)
        wb = xl.load_workbook(self.path)
        ws = wb.active
        ws.delete_cols(idx = 1)
        wb.save(self.path)
   
    def import_metrics(self):
        df = pd.read_excel(self.path)
        metrics = df.to_dict('records')
        return metrics