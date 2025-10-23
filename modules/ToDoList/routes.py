from flask import Blueprint, render_template, request, redirect, url_for
from modules.ToDoList.data import tasks

ToDoList_bp = Blueprint("ToDoList", __name__, template_folder="templates", static_folder="static")

# Список завдань
@ToDoList_bp.route("/")
def index():
    return render_template("ToDoList_index.html", tasks=tasks)

# Додавання завдань
@ToDoList_bp.route("/add", methods=["POST"])
def add_task():
    new_id = max([t["id"] for t in tasks]) + 1 if tasks else 1
    tasks.append({
        "id": new_id,
        "title": request.form["title"],
        "description": request.form["description"],
        "deadline": request.form["deadline"],
        "status": request.form["status"]
    })
    return redirect(url_for("ToDoList.index"))

# Видалення
@ToDoList_bp.route("/delete/<int:id>")
def delete_task(id):
    global tasks
    tasks[:] = [t for t in tasks if t["id"] != id]
    return redirect(url_for("ToDoList.index"))

# Редагування
@ToDoList_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    task = next((t for t in tasks if t["id"] == id), None)
    if request.method == "POST" and task:
        task["description"] = request.form["description"]
        task["deadline"] = request.form["deadline"]
        task["status"] = request.form["status"]
        return redirect(url_for("ToDoList.index"))
    return render_template("ToDoList_edit.html", task=task)
