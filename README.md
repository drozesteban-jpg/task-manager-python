# Task Manager CLI (Python)

Simple administrador de tareas por línea de comandos, desarrollado en Python.

---

## Features

- Agregar tareas
- Listar tareas
- Marcar tareas como completadas
- Eliminar tareas
- Ver tareas pendientes y completadas
- Persistencia de datos en archivo JSON

---

## Requisitos

- Python 3.8 o superior

---

## Como ejecutar

Clonar el repositorio:

    git clone https://github.com/drozesteban-jpg/task-manager-python.git
 cd task-manager-python



Ejecutar el programa:

    python3 main.py

---

## Project Structure

    task_manager_python/
    ├── main.py
    ├── tasks.json
    ├── requirements.txt
    ├── README.md
    ├── task_manager/
    │   ├── __init__.py
    │   ├── cli.py
    │   ├── tasks.py
    │   └── storage.py
    └── tests/
        └── test_tasks.py

---

## Como funciona

Las tareas se almacenan en el archivo tasks.json.

Cada tarea contiene:
- id
- titulo
- fecha de creacion
- estado (pendiente o completada)

El programa carga el archivo al iniciar y guarda los cambios automaticamente.

---

## Autor

Esteban Droz

Proyecto de practica en Python para consolidar:
- logica
- manejo de archivos
- estructuras de datos
- uso real de Git y GitHub




























