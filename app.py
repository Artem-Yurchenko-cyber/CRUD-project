from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Дані зберігаються у пам'яті
books = [
    {"id": 1, "title": "Мистецтво війни", "author": "Сунь-цзи", "pages": 180, "status": "Прочитано"},
    {"id": 2, "title": "1984", "author": "Джордж Орвелл", "pages": 328, "status": "Не прочитано"},
]
# next_id = 3
next_id = max(b["id"] for b in books) + 1 if books else 1

@app.route("/")
def index():
    return render_template("index.html", books=books)

@app.route("/add", methods=["POST"])
def add_book():
    global next_id
    title = request.form["title"]
    author = request.form["author"]
    pages = request.form["pages"]
    status = request.form["status"]

    books.append({
        "id": next_id,
        "title": title,
        "author": author,
        "pages": pages,
        "status": status
    })
    next_id += 1

    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    book = next((b for b in books if b["id"] == id), None)

    if request.method == "POST":
        if book:
            book["title"] = request.form["title"]
            book["author"] = request.form["author"]
            book["pages"] = request.form["pages"]
            book["status"] = request.form["status"]
        return redirect(url_for("index"))

    return render_template("edit.html", book=book)

# Запуск сервера
if __name__ == "__main__":
    # debug = True -> сервер перехапускає
    app.run(debug=True)