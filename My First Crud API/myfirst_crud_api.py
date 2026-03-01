from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author": self.author,
            "publisher": self.publisher,
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Book API is running!"


# CREATE (POST)
@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json() or {}

    required = ["book_name", "author", "publisher"]
    missing = [x for x in required if x not in data or not str(data[x]).strip()]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Prevent duplicate book_name
    if Book.query.filter_by(book_name=data["book_name"].strip()).first():
        return jsonify({"error": "book_name already exists"}), 409

    book = Book(
        book_name=data["book_name"].strip(),
        author=data["author"].strip(),
        publisher=data["publisher"].strip(),
    )
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201


# READ ALL (GET)
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify({"books": [b.to_dict() for b in books]})


# READ ONE (GET)
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())


# UPDATE (PUT)
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json() or {}

    if "book_name" in data:
        new_name = data["book_name"].strip()
        if new_name != book.book_name and Book.query.filter_by(book_name=new_name).first():
            return jsonify({"error": "book_name already exists"}), 409
        book.book_name = new_name

    if "author" in data:
        book.author = data["author"].strip()

    if "publisher" in data:
        book.publisher = data["publisher"].strip()

    db.session.commit()
    return jsonify(book.to_dict())


# DELETE (DELETE)
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)