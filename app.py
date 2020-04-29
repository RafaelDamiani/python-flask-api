from flask import Flask, jsonify, request, Response

from BookModel import *
from settings import *
import json

@app.route('/books')
def get_books():
    return jsonify({'books': Book.get_all_books()})

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = Book.get_book(isbn)
    return jsonify(return_value)

@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()    
    if(validBookObject(request_data)):
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'])
        books.insert(0, new_book)
        reponse = Response("", 201, mimetype='application/json')
        reponse.headers['Location'] = "/books/" + str(request_data['isbn'])
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
    request_data = request.get_json()
    if(not validPutBookObject(request_data)):
        invalidBookObjecterrorMsg = {
            "error": "Valid book object must be passed to the request",
            "helpString": "Check the params passed and try again"
        }
        response = Response(json.dumps(invalidBookObjecterrorMsg), status=400, mimetype='application/json')
        return response

    Book.replace_book(isbn, request_data['name'], request_data['price'])
    response = Response("", status=204)
    return response

@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if ("name" in request_data):
        Book.update_book_name(isbn, request_data['name'])
    if ("price" in request_data):
        Book.update_book_price(isbn, request_data['price'])

    response = Response("", status=204)
    response.headers['Location'] = "/books/" + str(isbn)
    return response

@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    if (Book.delete_book(isbn)):
        response = Response("", status=204)
        return response

    invalidBookObjecterrorMsg = {
        "error": "Book with the ISBN number that was provided was not found."
    }
    response = Response(json.dumps(invalidBookObjecterrorMsg), status=404, mimetype="application/json")
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