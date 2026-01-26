from datetime import datetime


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(tasks, title):
    task = {
        "id": get_next_id(tasks),
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    return task


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def complete_task(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task:
        task["done"] = True
        return True
    return False


def delete_task(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task:
        tasks.remove(task)
        return True
    return False

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.json"


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
def list_tasks(tasks):
    if not tasks:
        print("📭 No hay tareas.")
        return

    for task in tasks:
        status = "✅" if task["done"] else "⏳"
        print(f'{status} [{task["id"]}] {task["title"]}')

print("tasks.py cargado correctamente")
