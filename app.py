from flask import Flask, jsonify

stores = [{
    'name': 'Store One',
    'items': [{'name':'Paper A4', 'price': 0.99 }]
}]

app = Flask(__name__)

# Endpoints with GET, POST methods
# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/itme')
def get_itme_in_store(name):
    pass

app.run(port=4000)
