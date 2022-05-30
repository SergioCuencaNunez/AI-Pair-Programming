class Unit_Test:
    def __init__(self, test_id, test):
        self._test_id = test_id
        self._test = test

    def get_test_id(self):
            return self._test_id

    def get_test(self):
        return self._test
    
    def set_test_id(self, value):
        self._test_id = value
    
    def set_test(self, value):
        self._test = value
    
    def __str__(self):
        return self._test_id + ", " + self._test 

