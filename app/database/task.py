from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        res = {
            "id": result[0],
            "name": result[1],
            "summary": result[2],
            "description": result[3],
            "is_done": result[4]
        }
        out.append(res)
    return out

def scan():
    try:
        conn = get_db()
        cursor = conn.execute("SELECT * FROM task")
        results = cursor.fetchall()
        return output_formatter(results)
    except Exception as e:
        print(f"Error during scan: {e}")
        return []

def select_by_id(task_id):
    try:
        conn = get_db()
        cursor = conn.execute("SELECT * FROM task WHERE id=?", (task_id,))
        results = cursor.fetchall()
        if results:
            return output_formatter(results)[0]
        return {}
    except Exception as e:
        print(f"Error during select_by_id: {e}")
        return {}

def insert(task_data):
    if not all(k in task_data for k in ("name", "summary", "description")):
        raise ValueError("task_data must contain 'name', 'summary', and 'description'")

    task_tuple = (
        task_data["name"],
        task_data["summary"],
        task_data["description"]
    )

    statement = """
        INSERT INTO task (name, summary, description) VALUES (?, ?, ?)
    """
    try:
        conn = get_db()
        with conn:
            conn.execute(statement, task_tuple)
    except Exception as e:
        print(f"Error during insert: {e}")

def update_by_id(task_data, task_id):
    if not all(k in task_data for k in ("name", "summary", "description", "is_done")):
        raise ValueError("task_data must contain 'name', 'summary', 'description', and 'is_done'")

    task_tuple = (
        task_data["name"],
        task_data["summary"],
        task_data["description"],
        task_data["is_done"],
        task_id
    )

    statement = """
    UPDATE task SET
        name = ?,
        summary = ?,
        description = ?,
        is_done = ?
    WHERE id = ?
    """
    try:
        conn = get_db()
        with conn:
            conn.execute(statement, task_tuple)
    except Exception as e:
        print(f"Error during update_by_id: {e}")

def delete_by_id(task_id):
    try:
        conn = get_db()
        with conn:
            conn.execute("DELETE FROM task WHERE id=?", (task_id,))
    except Exception as e:
        print(f"Error during delete_by_id: {e}")
