from flask import Flask, request, jsonify
from flask_cors import CORS
from tinydb import TinyDB, Query
from uuid import uuid4

app = Flask(__name__)
CORS(app)
db = TinyDB("tasks.json")


@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def home():
    if request.method == "GET":
        # Returns all tasks
        return {"success": True, "tasks": db.all()}

    elif request.method == "POST":
        # Creates a new task and insert it to database
        data = request.get_json()
        if "title" not in data:
            return {"success": False, "message": "title not provided"}
        id = str(uuid4())
        db.insert({"id": id, "title": data["title"], "completed": False})
        res = db.search(Query().id == id)[0]
        res["success"] = True
        return res

    elif request.method == "PUT":
        # Toggles completed of a task
        data = request.get_json()
        if "id" not in data:
            return {"success": False, "message": "id not provided"}
        q = db.search(Query().id == data["id"])
        if len(q) == 0:
            return {"success": False, "message": "task not found"}
        db.update({"completed": not q[0]["completed"]}, Query().id == data["id"])
        return {"success": True}

    elif request.method == "DELETE":
        # Deletes a task
        data = request.get_json()
        if "id" not in data:
            return {"success": False, "message": "id not provided"}
        q = db.search(Query().id == data["id"])
        if len(q) == 0:
            return {"success": False, "message": "task not found"}
        db.remove(Query().id == data["id"])
        return {"success": True}

    else:
        return {"success": False, "message": "Bad method"}
