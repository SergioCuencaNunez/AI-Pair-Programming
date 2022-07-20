import sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

#class FileCSV_Mock:
#    def __init__(self, path):
#        self.path = path

#    def get_lines(self):
#        return "file_contents_csv"

#class FileTXT_Mock:
#    def __init__(self, path):
#        self.path = path
        
#    def get_lines():
#        return "file_contents_txt"

#class Graph_Mock:
#    def __init__(self, data):
#        self.data = data

def test0():
    from ai_unit_testing.code_under_test import RouteDomain
    filepath = "files/input-file-test.csv"
    route_domain = RouteDomain(filepath)
    assert route_domain.file == "files/input-file-test.csv"
    
def test1():
    from ai_unit_testing.code_under_test import RouteDomain
    from ai_unit_testing.code_under_test import FileCSV
    filepath = "files/input-file-test.csv"
    route_domain = RouteDomain(filepath)
    assert route_domain.file == "files/input-file-test.csv"
    assert route_domain.file_entity.__class__.__name__ == "FileCSV"

def test2():
    from ai_unit_testing.code_under_test import RouteDomain
    from ai_unit_testing.code_under_test import FileCSV
    from ai_unit_testing.code_under_test import Graph
    filepath = "files/input-file-test.csv"
    route_domain = RouteDomain(filepath)
    assert route_domain.file == "files/input-file-test.csv"
    assert route_domain.file_entity.__class__.__name__ == "FileCSV"
    assert route_domain.graph.__class__.__name__ == "Graph"