from flask import Flask, render_template, url_for
import json
from modules.library.routes import library_bp
from modules.cinema.routes import cinema_bp
from modules.ToDoList.routes import ToDoList_bp

app = Flask(__name__)

# Підключення blueprint'ів
app.register_blueprint(library_bp, url_prefix="/library")
app.register_blueprint(cinema_bp, url_prefix="/cinema")
app.register_blueprint(ToDoList_bp, url_prefix="/ToDolist")

# Завантаження списку модулів
def load_modules():
    with open("data/modules.json", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    modules = load_modules()
    return render_template("home.html", modules=modules)

if __name__ == "__main__":
    app.run(debug=True)
