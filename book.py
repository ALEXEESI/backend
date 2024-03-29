from flask import Flask,jsonify

app = Flask(__name__)
books = [
    {"ID" :1,"title":"Book 1","author":"Author 1"},
    {"ID" :2,"title":"Book 2","author":"Author 2"},
    {"ID" :3,"title":"Book 3","author":"Author 3"},
    {"ID" :3,"title":"Book 3","author":"Author 3"}
]

@app.route("/")
def Greef():
    return "<p>Welcome to Book Management Systems</p>"

@app.route("/books",methods=[("GET")])
def get_all_books():
    return jsonify({"books":books})

@app.route("/books/<int:book_id>",methods=["GET"])
def get_book(book_id):
    book=next( (b for b in books if b["id"]==book_id),None)
    if book:
        return jsonify(book)
    else :
        return jsonify({"error":"Book not found"}),404

if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=5000,debug=True)


