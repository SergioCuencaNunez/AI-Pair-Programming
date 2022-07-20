import unittest, importlib
from unittest.mock import patch
from unittest.mock import Mock
import mongomock

import sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

import ai_unit_testing.code_under_test as code_under_test 
#app = code_under_test.app
    
def test_user_post():
    importlib.reload(code_under_test)
    app = code_under_test.app
    
    def insert_mock(data):
        assert data["name"] == "Sergio"
        assert data["designation"] == "Accenture"
        return 1

    # POST
    client = app.test_client()
    mock_db = mongomock.MongoClient().db.collection
    mock_db.insert = insert_mock
    mock_db.find_one = Mock(return_value = {"name": "Sergio", "designation": "Accenture"})
    
    with patch("ai_unit_testing.code_under_test.mongo.db.users", new = mock_db):
        response = client.post("/user", json = {
            "name": "Sergio",
            "designation": "Accenture",
        })
        assert response.status_code == 200

def test_user_get_one():
    importlib.reload(code_under_test)
    app = code_under_test.app

    def find_mock(data):
        assert data["name"] == "Sergio"
        assert data["designation"] == "Accenture"
        return [{"name" : "Sergio", "designation" : "Accenture"}]

    def find_one_mock(data):
        assert data["name"] == "Sergio"
        assert data["designation"] == "Accenture"
        return {"name" : "Sergio", "designation" : "Accenture"}

    # GET
    client = app.test_client()
    mock_db = mongomock.MongoClient().db.collection
    mock_db.find_one = find_one_mock
    mock_db.find = find_mock

    with patch("ai_unit_testing.code_under_test.mongo.db.users", new = mock_db):
        query = {"name": "Sergio", "designation": "Accenture"}
        response = client.get("/user", query_string = query)
        assert response.status_code == 200
        assert response.json["result"] == [{"name": "Sergio", "designation": "Accenture"}] or response.json["result"] == {"name": "Sergio", "designation": "Accenture"}


def test_user_get_all():
    importlib.reload(code_under_test)
    app = code_under_test.app

    def find_mock(data):
        return [{"name" : "Sergio", "designation" : "Accenture"}, {"name" : "María", "designation" : "Accenture"}]

    # GET
    client = app.test_client()
    mock_db = mongomock.MongoClient().db.collection
    mock_db.find = find_mock
    
    with patch("ai_unit_testing.code_under_test.mongo.db.users", new = mock_db):
        response = client.get("/users")
        assert response.status_code == 200
        assert response.json["result"] == [{"name" : "Sergio", "designation" : "Accenture"}, {"name" : "María", "designation" : "Accenture"}]
