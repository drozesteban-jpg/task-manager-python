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
