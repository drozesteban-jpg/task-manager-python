from task_manager.tasks import (
    load_tasks,
    save_tasks,
    add_task,
    list_tasks,
    complete_task,
    delete_task
)


def show_menu():
    print("\n📋 Task Manager")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    while True:
        show_menu()
        choice = input("Elegí una opción: ").strip()

        if choice == "1":
            tasks = load_tasks()
            list_tasks(tasks)

        elif choice == "2":
            tasks = load_tasks()
            title = input("📝 Título de la tarea: ")
            add_task(tasks, title)
            save_tasks(tasks)
            print("✅ Tarea agregada.")

        elif choice == "3":
            tasks = load_tasks()
            task_id = int(input("🆔 ID de la tarea a completar: "))

            if complete_task(tasks, task_id):
                save_tasks(tasks)
                print("✅ Tarea marcada como completada.")
            else:
                print("❌ No se encontró una tarea con ese ID.")

        elif choice == "4":
            tasks = load_tasks()
            task_id = int(input("🆔 ID de la tarea a eliminar: "))

            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print("🗑️ Tarea eliminada.")
            else:
                print("❌ No se encontró una tarea con ese ID.")

        elif choice == "5":
            print("👋 Chau!")
            break

        else:
            print("❌ Opción inválida. Probá de nuevo.")


if __name__ == "__main__":
    main()
