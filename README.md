Task Manager CLI (Python)
Aplicación simple de línea de comandos para gestionar tareas.
Permite crear, listar, completar y eliminar tareas, guardándolas en un archivo JSON.
Proyecto realizado como práctica de Python, modularización y testing básico.
Cómo ejecutar el programa
Desde la carpeta raíz del proyecto, ejecutar:
python3 main.py
Qué se puede hacer
Agregar tareas
Ver todas las tareas
Marcar tareas como completadas
Eliminar tareas
Ver tareas pendientes
Ver tareas completadas
Las tareas se guardan automáticamente en el archivo tasks.json.
Ejecutar los tests
Desde la raíz del proyecto:
python3 tests/test_tasks.py
Estructura del proyecto
task_manager_python/
│
├── main.py
├── task_manager/
│ ├── cli.py
│ ├── tasks.py
│ └── storage.py
├── tests/
│ └── test_tasks.py
└── tasks.json
Autor
Esteban










































