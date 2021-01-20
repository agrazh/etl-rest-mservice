from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="Item name is required.")
    parser.add_argument('priority',
        type=float,
        # required=True,
        help="Item priority is required.")
    parser.add_argument('queue_id',
        type=int,
        # required=True,
        help="Queue id is required.")

    @jwt_required()
    def get(self):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(data['name'])
        if item:
            return item.json()
        return {'message': 'Item not found.'}, 404

    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()

        if ItemModel.find_by_name(data['name']):
            return {'message': "An item with a name '{}' already exists.".format(data['name'])}, 400

        item = ItemModel(data['name'], data['priority'], data['queue_id'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(data['name'])
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}

        return {'message': 'Item not found.'}

    @jwt_required()
    def put(self):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(data['name'])
        if item is None:
            item = ItemModel(data['name'], data['priority'], data['queue_id'])
        else:
            item.priority = data['priority']
            item.queue_id = data['queue_id']
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
