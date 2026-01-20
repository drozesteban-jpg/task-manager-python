# 🗂 Task Manager CLI (Python)

Simple administrador de tareas por línea de comandos, desarrollado en Python.

---

## 🚀 Features

- Agregar tareas
- Listar todas las tareas
- Marcar tareas como completadas
- Eliminar tareas
- Ver tareas pendientes y completadas
- Persistencia de datos en archivo JSON

---

## 🛠 Requisitos

- Python 3.8 o superior

---

## ▶️ Cómo ejecutar


Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/task-manager-cli.git
cd task-manager-cli


## Project Structure

```text
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


##Ejecuta el programa:
 
 python3 main.py


##Cómo funciona
Las tareas se almacenan en un archivo tasks.json.
Cada tarea contiene:
-id
-título
-fecha de creación
-estado (pendiente / completada)
El programa carga el archivo al iniciar y guarda los cambios automáticamente.


##Autor
Esteban Droz

Proyecto de práctica en Python para consolidar:
lógica
manejo de archivos
estructuras de datos
uso real de Git y GitHub





























