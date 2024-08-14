from flask import Flask, request, jsonify
from app.database import task  # Ensure this import is correct and the methods are defined

app = Flask(__name__)

# HTTP GET METHOD
@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    tasks_list = task.scan()  # Assuming task.scan() returns a list of tasks
    return jsonify({"tasks": tasks_list, "ok": True})

# HTTP POST METHOD
@app.route("/tasks", methods=["POST"])
def create_task():
    task_data = request.json
    task.insert(task_data)  # Assuming task.insert() correctly inserts the task into the database
    return "", 204

# HTTP PUT METHOD
@app.route("/tasks/<int:pk>", methods=["PUT"])
def update_task(pk):
    task_data = request.json
    task.update_by_id(pk, task_data)  # Assuming task.update_by_id(pk, task_data) updates the task
    return "", 204

# HTTP DELETE METHOD
@app.route("/tasks/<int:pk>", methods=["DELETE"])
def delete_task(pk):
    task.delete_by_id(pk)  # Assuming task.delete_by_id(pk) deletes the task
    return "", 204

if __name__ == '__main__':
    app.run(port=5000)  # Consider using environment variables for port configuration

