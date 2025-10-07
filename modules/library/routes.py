from flask import Blueprint, render_template, request, redirect, url_for
from modules.library.data import books

library_bp = Blueprint("library", __name__, template_folder="templates", static_folder="static")

# Список книг
@library_bp.route("/")
def index():
    return render_template("library_index.html", books=books)

# Додавання книги
@library_bp.route("/add", methods=["POST"])
def add_book():
    new_id = max([b["id"] for b in books]) + 1 if books else 1
    books.append({
        "id": new_id,
        "title": request.form["title"],
        "author": request.form["author"],
        "pages": request.form["pages"],
        "status": request.form["status"]
    })
    return redirect(url_for("library.index"))

# Видалення
@library_bp.route("/delete/<int:id>")
def delete_book(id):
    global books
    books[:] = [b for b in books if b["id"] != id]
    return redirect(url_for("library.index"))

# Редагування
@library_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if request.method == "POST" and book:
        book["title"] = request.form["title"]
        book["author"] = request.form["author"]
        book["pages"] = request.form["pages"]
        book["status"] = request.form["status"]
        return redirect(url_for("library.index"))
    return render_template("library_edit.html", book=book)
