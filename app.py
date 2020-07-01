from flask import Flask, request
from flask_restful import Resource, Api

items = []

app = Flask(__name__)
api = Api(app)

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404
    
    def post(self, name):
        data = request.get_json() # force=False, silent=False
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'item': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=4000, debug=True)
