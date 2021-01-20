from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.queue import Queue, QueueList

import yaml

with open('./config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cache.db'
app.config['SQLALCHEMY_BINDS'] = {
    # 'postgresql+psycopg2://db_user:db_pw@localhost:5432/db_name'
    'PostgreSQL': 'postgresql+psycopg2://' + config.get('PostgreSQL')['conn_string'],
    # 'mysql+pymysql://db_user:db_pw@localhost:3306/db_name'
    'MySQL': 'mysql+pymysql://' + config.get('MySQL')['conn_string']
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = config.get('secret_key')
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth endpoint

# # automatically create sqlite cache based on your models
# @app.before_first_request
# def init_cache():
#     db.create_all()

if config.get('user_registration_api'):
    api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item')
api.add_resource(ItemList, '/items')
api.add_resource(Queue, '/queue/<string:name>')
api.add_resource(QueueList, '/queues')

if __name__ == '__main__':
    from db import db
    from init_cache import init_cache

    init_cache()
    db.init_app(app)
    app.run(port=(config.get('port') or 4000), debug=(config.get('debug') or False))
