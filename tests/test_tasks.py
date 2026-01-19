from task_manager.tasks import (
    get_next_id,
    add_task,
    find_task_by_id,
    complete_task,
    delete_task,
)


def test_get_next_id():
    tasks = [{"id": 1}, {"id": 2}]
    assert get_next_id(tasks) == 3


def test_add_task():
    tasks = []
    task = add_task(tasks, "Test task")
    assert task["id"] == 1
    assert task["title"] == "Test task"
    assert task["done"] is False


def test_find_task_by_id():
    tasks = [{"id": 1, "title": "Hola", "done": False}]
    task = find_task_by_id(tasks, 1)
    assert task is not None


def test_complete_task():
    tasks = [{"id": 1, "done": False}]
    result = complete_task(tasks, 1)
    assert result is True
    assert tasks[0]["done"] is True


def test_delete_task():
    tasks = [{"id": 1}]
    result = delete_task(tasks, 1)
    assert result is True
    assert tasks == []
