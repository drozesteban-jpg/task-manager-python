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

def ask_task_id():
    value = input("🆔 ID de la tarea: ").strip()

    if not value.isdigit():
        print("❌ Ingresá un número válido.")
        return None

    return int(value)


def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Elegí una opción: ").strip()

        if choice == "1":
            
            list_tasks(tasks)

        elif choice == "2":
            
            title = input("📝 Título de la tarea: ").strip()

            if not title:
              print("❌ El título no puede estar vacío.")
              continue

            add_task(tasks, title)
            save_tasks(tasks)
            print("✅ Tarea agregada.")

        elif choice == "3":
            
            task_id = ask_task_id()
            if task_id is None:
             continue


            if complete_task(tasks, task_id):
                save_tasks(tasks)
                print("✅ Tarea marcada como completada.")
            else:
                print("❌ No se encontró una tarea con ese ID.")

        elif choice == "4":
            task_id = ask_task_id()
            if task_id is None:
               continue

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
