import importlib

from ai_unit_testing.unit_test import Unit_Test

class Unit_Test_Dummy(Unit_Test):
    def __init__(self, problem_id, file, function):
        super().__init__(problem_id, file, function)

    def apply_test(self, problem, solution):
        test_module = importlib.import_module(f"ai_data.tests.{self.get_file()}")
        test_function = getattr(test_module, self.get_function())
        
        check_program = (
            problem.get_prompt() + solution.get_solution() #+ "\n" +
        #    test_function + "\n" +
        #    #f"check({problem.get_entry_point()})" + "\n"
        #    problem.get_entry_point() + "\n"
        )

        return self._execute_test(test_function, check_program)

    def _execute_test(self, test, program):

        try:
            test(program)
            #print(program)
            return True
        except Exception as e:
            print(e)
            print(program)
            print("\n"*5)
            return False
