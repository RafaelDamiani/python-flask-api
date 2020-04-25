from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        'name': 'The Mythical Man-Month',
        'price': 32.85,
        'isbn': 9873218168
    },
    {
        'name': 'Clean Code',
        'price': 60.42,
        'isbn': 6549815352
    },
]

#
@app.route('/books')
def get_books():
    return jsonify({'books': books})

app.run(port=5000)