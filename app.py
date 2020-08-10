from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

items = []

app = Flask(__name__)
app.secret_key = 'tmp_key' # temporary implementation
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates a new endpoint /auth

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with a name '{}' already exists.".format(name)}, 400

        data = request.get_json() # force=False, silent=False
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

api.add_resource(Item, '/item/<string:name>')

class ItemList(Resource):
    def get(self):
        return {'item': items}

api.add_resource(ItemList, '/items')

app.run(port=4000, debug=True)
