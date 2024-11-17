from flask import Flask, jsonify
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# tiny DB
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# tiny DB
TASKS = [
    {
        'task': 'Bake Bread',
        'done': False
    },
        {
        'task': 'Make a CRUD App',
        'done': True
    },
    {
        'task': 'Soccer Practice',
        'done': False
    }
]

#book
@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })

#tasks
@app.route('/tasks', methods=['GET'])
def all_tasks():
    return jsonify({
        'status': 'success',
        'tasks': TASKS
    })


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
