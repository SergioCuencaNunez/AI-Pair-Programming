from ai_unit_testing.unit_test import Unit_Test

class Unit_Test_Dummy(Unit_Test):
    def __init__(self, problem_id, test):
        super().__init__(problem_id, test)

    def apply_test(self, problem, solution):
        check_program = (
            problem.get_prompt() + solution.get_solution() + "\n" +
            self.get_test() + "\n" +
            f"check({problem.get_entry_point()})" + "\n"
        )

        return self._execute_test(check_program)

    def _execute_test(self, program):
        try:
            exec(program)
            return True
        except BaseException:
            return False

