import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✖"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Nueva tarea: ")
    tasks.append({"title": title, "done": False})

def complete_task(tasks):
    show_tasks(tasks)
    index = int(input("Número de tarea completada: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Número de tarea a eliminar: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        option = input("Elegí una opción: ")

        if option == "1":
            show_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            save_tasks(tasks)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
