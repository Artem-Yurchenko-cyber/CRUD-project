from flask import Blueprint, render_template, request, redirect, url_for
from modules.cinema.data import movies

cinema_bp = Blueprint("cinema", __name__, template_folder="templates", static_folder="static")

# Список фільмів
@cinema_bp.route("/")
def index():
    return render_template("cinema_index.html", movies=movies)

# Додавання фільмів
@cinema_bp.route("/add", methods=["POST"])
def add_movie():
    new_id = max([m["id"] for m in movies]) + 1 if movies else 1
    movies.append({
        "id": new_id,
        "title": request.form["title"],
        "country": request.form["country"],
        "year": request.form["year"],
        "duration": request.form["duration"],
        "status": request.form["status"]
    })
    return redirect(url_for("cinema.index"))

# Видалення фільмів
@cinema_bp.route("/delete/<int:id>")
def delete_movie(id):
    global movies
    movies[:] = [m for m in movies if m["id"] != id]
    return redirect(url_for("cinema.index"))

# Редагування фільмів
@cinema_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_movie(id):
    movie = next((m for m in movies if m["id"] == id), None)
    if request.method == "POST" and movie:
        movie["title"] = request.form["title"]
        movie["country"] = request.form["country"]
        movie["year"] = request.form["year"]
        movie["duration"] = request.form["duration"]
        movie["status"] = request.form["status"]
        return redirect(url_for("cinema.index"))
    return render_template("cinema_edit.html", movie=movie)