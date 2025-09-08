from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "Мистецтво війни", "author": "Сунь-цзи", "pages": 180, "status": "Прочитано"},
    {"id": 2, "title": "1984", "author": "Джордж Орвелл", "pages": 328, "status": "Не прочитано"},
]

@app.route("/")
def index():
    return render_template("index.html", books=books)

# Create
@app.route("/add", methods=["POST"])
def add_book():
    new_id = max([b["id"] for b in books]) + 1 if books else 1
    title = request.form["title"]
    author = request.form["author"]
    pages = request.form["pages"]
    status = request.form["status"]
    books.append({"id": new_id, "title": title, "author": author, "pages": pages, "status": status})
    return redirect(url_for("index"))

# Update
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return "Book not found", 404

    if request.method == "POST":
        book["title"] = request.form["title"]
        book["author"] = request.form["author"]
        book["pages"] = request.form["pages"]
        book["status"] = request.form["status"]
        return redirect(url_for("index"))

    return render_template("edit.html", book=book)

# Delete
@app.route("/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)