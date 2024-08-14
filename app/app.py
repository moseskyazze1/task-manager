# Save this code in app.py and run it with `python app.py`
from flask import Flask, request

app = Flask(__name__)

@app.route('/tasks', methods=['POST'])
def create_task():
    task_data = request.get_json()
    print(f"Received task data: {task_data}")
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
