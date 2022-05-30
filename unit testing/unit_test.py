class Unit_Testing:
    def __init__(self, test_id, canonical_solution):
        self._test_id = test_id
        self._canonical_solution = canonical_solution

    def get_test_id(self):
            return self._test_id

    def get_canonical_solution(self):
        return self._canonical_solution
    
    def set_test_id(self, value):
        self._test_id = value
    
    def set_canonical_solution(self, value):
        self._canonical_solution = value
    
unit_test = Unit_Testing("test/0", "return x")
