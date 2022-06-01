class Unit_Test:
    def __init__(self, test_id, test):
        self.test_id = test_id
        self.test = test

    def get_test_id(self):
            return self.test_id

    def get_test(self):
        return self.test
    
    def set_test_id(self, value):
        self.test_id = value
    
    def set_test(self, value):
        self.test = value
