class Unit_Testing:
    def __init__(self, test_id, canonical_solution, entry_point):
        self._test_id = test_id
        self._canonical_solution = canonical_solution
        self._entry_point = entry_point

    def get_test_id(self):
            return self._test_id

    def get_canonical_solution(self):
        return self._canonical_solution

    def get_entry_point(self):
        return self._entry_point
    
    def set_test_id(self, value):
        self._test_id = value
    
    def set_canonical_solution(self, value):
        self._canonical_solution = value
    
    def set_entry_point(self, value):
        self._entry_point = value

unit_test = Unit_Testing("test/0", "return x", "return_x(x)")
