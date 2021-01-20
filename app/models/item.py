from db import db

class ItemModel(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # priority = db.Column(db.Float(precision=1))
    priority = db.Column(db.Integer)

    queue_id = db.Column(db.Integer, db.ForeignKey('queue.id'))
    queue = db.relationship('QueueModel')

    def __init__(self, name, priority, queue_id):
        self.name = name
        self.priority = priority
        self.queue_id = queue_id

    def json(self):
        return {'name': self.name, 'priority': self.priority, 'queue_id': self.queue_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
