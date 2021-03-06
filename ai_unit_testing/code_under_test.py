from flask import Flask ,request,jsonify, make_response
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
app = Flask(__name__)
api=Api(app)
app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://db:27017/restdb'
mongo = PyMongo(app)

class User(Resource):
    def get(self):
        users = mongo.db.users
        users = users.find({"name":request.args.get("name"),"designation":request.args.get("designation")})
        return jsonify(users)

api.add_resource(User, '/users')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)
app.config['MONGO_DBNAME'] ='restdb'
app.config['MONGO_URI'] ='mongodb://db:27017/restdb'
mongo = PyMongo(app)

