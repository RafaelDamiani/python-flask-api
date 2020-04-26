from flask import Flask, jsonify, request, Response
import json
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
                "name": book["name"],
                "price": book["price"]
            }
    return jsonify(return_value)

@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()    
    if(validBookObject(request_data)):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        reponse = Response("", 201, mimetype='application/json')
        reponse.headers['Location'] = "/books/" + str(new_book['isbn'])
        return reponse
    else:
        invalidBookObjecterrorMsg = {
            "error": "Invalid book passed in request",
            "helpString": "Check the params passed and try again"
        }
        response = Response(json.dumps(invalidBookObjecterrorMsg), status=400, mimetype='application/json')
        return response

@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = (request.get_json())
    if(not validPutBookObject(request_data)):
        invalidBookObjecterrorMsg = {
            "error": "Valid book object must be passed to the request",
            "helpString": "Check the params passed and try again"
        }
        response = Response(json.dumps(invalidBookObjecterrorMsg), status=400, mimetype='application/json')
        return response

    replaced_book = {
        'name': request_data['name'],
        'price': request_data['price'],
        'isbn': isbn
    }
    i = 0
    for book in books:
        currentIsbn = book['isbn']
        if currentIsbn == isbn:
            books[i] = replaced_book
        i += 1
    response = Response("", status=204)
    return response

@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if ("name" in request_data):
        updated_book['name']
    if ("price" in request_data):
        updated_book['price']
    for book in books:
        if book['isbn'] == isbn:
            book.update(updated_book)
    response = Response("", status=204)
    response.headers['Location'] = "/books/" + str(isbn)
    return response

def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

def validPutBookObject(bookObject):
    if("name" in bookObject and "price" in bookObject):
        return True
    else:
        return False

app.run(port=5000)