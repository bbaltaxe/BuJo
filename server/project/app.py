from flask import Flask, jsonify, request
from flask_cors import CORS
import db_utils 


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#initialize DB 
db_utils.create_db()

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
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

#tasks
@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        task = post_data.get('task')


        # # post with sqlite 
        # conn = sqlite3.connect(dbfile)
        # c = conn.cursor()
        # c.execute('INSERT INTO tasks (task) VALUES (?)', (task),)
        # conn.commit()
        # conn.close()

        # post with no db
        TASKS.append({
                'task': post_data.get('task'), 
                'done': False
            })
        response_object['message'] = 'Task added!'
    else: 
        response_object['tasks'] = TASKS
    return jsonify(response_object)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
