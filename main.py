import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(tasks):
    title = input("Escribí la nueva tarea: ").strip()
    if title:
        tasks.append({
            "title": title,
            "done": False
        })
        save_tasks(tasks)
        print("✅ Tarea agregada.")
    else:
        print("⚠️ La tarea no puede estar vacía.")



def list_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
        return

    pending = [t for t in tasks if not t["done"]]
    done = [t for t in tasks if t["done"]]

    print("\n📋 Tareas pendientes:")
    if not pending:
        print("✔️ Ninguna 🎉")
    else:
        for i, task in enumerate(pending, 1):
            print(f"{i}. ❌ {task['title']}")

    print("\n📋 Tareas completadas:")
    if not done:
        print("—")
    else:
        for i, task in enumerate(done, 1):
            print(f"{i}. ✔️ {task['title']}")




def complete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Número de tarea completada: "))
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("🎉 Tarea marcada como completada.")
    except (ValueError, IndexError):
        print("❌ Número inválido.")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("Número de tarea a eliminar: "))
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"🗑️ Tarea eliminada: {removed['title']}")
    except (ValueError, IndexError):
        print("❌ Número inválido.")



def show_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")



def main():
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("Elegí una opción: ").strip()

        if option == "1":
            add_task(tasks)
        elif option == "2":
            list_tasks(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            print("👋 Hasta luego")
            break
        else:
            print("❌ Opción inválida.")
if __name__ == "__main__":
    main()
