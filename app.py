from flask import Flask, render_template, redirect, url_for, json
from modules.library.routes import library_bp
from modules.cinema.routes import cinema_bp
from modules.ToDoList.routes import ToDoList_bp

app = Flask(__name__)

app.register_blueprint(library_bp, url_prefix="/library")
app.register_blueprint(cinema_bp, url_prefix="/cinema")
app.register_blueprint(ToDoList_bp, url_prefix="/ToDoList")

@app.route("/")
def home():
    with open("data/modules.json", "r", encoding="utf-8") as f:
        modules = json.load(f)
    return render_template("home.html", modules=modules)


if __name__ == "__main__":
    app.run(debug=True)