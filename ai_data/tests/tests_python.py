class FileCSV:
    def __init__(self, path):
        self.path = path

    def get_lines(self):
        return "file_contents_csv"

class FileTXT:
    def __init__(self, path):
        self.path = path
        
    def get_lines():
        return "file_contents_txt"

class Graph:
    def __init__(self, data):
        self.data = data

def test0(solution):
    exec(solution, globals())
    filepath = "files/input-file-test.csv"
    route_domain = RouteDomain(filepath)
    assert route_domain.file == "files/input-file-test.csv"

def test1(solution):
    exec(solution, globals())
    filepath = "files/input-file-test.csv"
    route_domain = RouteDomain(filepath)
    assert route_domain.file == "files/input-file-test.csv"
    assert route_domain.file_entity.__class__.__name__ == "FileCSV"

def test2(solution):
    exec(solution, globals())
    filepath = "files/input-file-test.csv"
    route_domain = RouteDomain(filepath)
    assert route_domain.file == "files/input-file-test.csv"
    assert route_domain.file_entity.__class__.__name__ == "FileCSV"
    assert route_domain.graph.__class__.__name__ == "Graph"
    assert graph.data == "file_contents_csv"