from flask_restful import Resource, Api

def test3(solution):
    exec(solution)
    user = User(Resource)    
    assert user.__class__.__name__ == "User"

def test4(solution):
    exec(solution)
    assert json.loads(get_all_stars())
    
def test5(solution):
    exec(solution)
    assert json.loads(get_one_star())
    
def test6(solution):
    exec(solution)
    assert json.loads(add_star())