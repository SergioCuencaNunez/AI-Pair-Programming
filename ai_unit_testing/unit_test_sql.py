from ai_unit_testing.unit_test import Unit_Test
import sqlite3

class Unit_Test_SQL(Unit_Test):
    def __init__(self, problem_id, test):
        super().__init__(problem_id, test)

    def apply_test(self, problem, solution):    
        return self._execute_test(solution.get_solution(), problem.get_canonical_solution(), self.get_test())

    def _execute_test(self, model_solution, canonical_solution, database):
        try:
            conn = sqlite3.connect(database)
            cur = conn.cursor()

            cur.execute(model_solution.lower())
            model_solution_res = cur.fetchall()

            cur.execute(canonical_solution.lower())
            canonical_solution_res = cur.fetchall()

            if(model_solution_res == canonical_solution_res):
                return True
            else:
                return False
            
        except BaseException:
            return False

