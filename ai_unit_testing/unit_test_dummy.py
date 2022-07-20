import importlib, shutil
import random as rm

from ai_unit_testing.unit_test import Unit_Test

class Unit_Test_Dummy(Unit_Test):
    def __init__(self, problem_id, file, function):
        super().__init__(problem_id, file, function)

    def apply_test(self, problem, solution):        
        check_program = (problem.get_prompt() + solution.get_solution())
        
        with open("ai_unit_testing/code_under_test.py","w") as f:
                f.writelines(check_program)
                
        return self._clean_program(check_program) and self._execute_test()

    def _execute_test(self):
        try:
            test_module = importlib.import_module(f"ai_data.tests.{self.get_file()}")
            test_function = getattr(test_module, self.get_function())
            test_function()
            #a = rm.randint(1, 1000)
            #shutil.copyfile("ai_unit_testing/code_under_test.py", f"gpt_neo_{a}")
            return True
        except Exception as e:
            print(e)
            #print(program)
            a = rm.randint(1, 1000)
            shutil.copyfile("ai_unit_testing/code_under_test.py", str(a))
            print("-"*60)
            print("\n"*5)
            return False
    
    def _clean_program(self, program):
        clean = False
        with open("ai_unit_testing/code_under_test.py","r") as f:
            lines = f.readlines()
        while len(lines) > 0 and not clean:
            try:
                with open("ai_unit_testing/code_under_test.py","w") as f:
                    f.writelines(lines)
                importlib.import_module("ai_unit_testing.code_under_test")
            except Exception as e:
                lines = lines[:-1]
            else:
                clean = True
                with open("ai_unit_testing/code_under_test.py","w") as f:
                    f.writelines(lines)
        return clean
