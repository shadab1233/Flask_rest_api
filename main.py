from flask import Flask, make_response, jsonify, request
app = Flask(__name__)

store={"1":{"id":1,"title":"white tiger","author":"arvind adiga"}}

@app.route('/')
def hello_world():
    return 'Hello, World!'
'''
5 routes are implemented for bookstore
1.) post /books to create new book record
2.) get /books to get all record of book
3.) put /books/<int id> to update specific book record
4.) get /books/<int id> to get information of specific book
5.) delete /books/<int id> to delete specific book  
'''
@app.route("/api/books", methods=["GET","POST"])
def book_store():
    if request.method =="GET":
        return make_response(jsonify(store),200)
    elif request.method == "POST":
        content = request.json
        book_id = content["id"]
        store[book_id] =content
        return make_response(jsonify(content),201)
        
@app.route("/api/book/<book_id>", methods=["GET","PUT","DELETE"])
def specific_book(book_id):
    if request.method == "GET":
        return make_response(jsonify(store[book_id],200))
    elif request.method == "PUT":
        content = request.json
        store[book_id] = content
        return make_response(jsonify(store[book_id],200))
    elif request.method == "DELETE":
        store.pop(book_id)
        return make_response(jsonify({}),200)


if __name__ == "__main__":
    app.run(debug=True)