from flask_restful import Resource
from models.queue import QueueModel

class Queue(Resource):
    def get(self, name):
        queue = QueueModel.find_by_name(name)
        if queue:
            return queue.json()
        return {'message': 'Queue not found'}, 404

    def post(self, name):
        if QueueModel.find_by_name(name):
            return {'message': "Queue with a name '{}' already exists.".format(name)}, 400

        queue = QueueModel(name)

        try:
            queue.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500 # Internal server error

        return queue.json(), 201

    def delete(self, name):
        queue = QueueModel.find_by_name(name)
        if queue:
            queue.delete_from_db()

        return {'message': 'Item deleted'}


class QueueList(Resource):
    def get(self):
        return {'queues': [queue.json() for queue in QueueModel.query.all()]}
