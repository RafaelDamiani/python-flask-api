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

@app.route('/books')
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                "price": book["price"]
            }
    return jsonify(return_value)

app.run(port=5000)