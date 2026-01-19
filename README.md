# Task Manager CLI (Python)

Simple command-line task manager built with Python.
Allows users to create, list, complete and delete tasks.
Tasks are stored locally in a JSON file.

This project was created as a Python practice project, focusing on:
- Code modularization
- File handling
- Basic unit testing

## How to run the program

From the root folder of the project, run:

python3 main.py

## Features

- Add tasks
- List all tasks
- Mark tasks as completed
- Delete tasks

All tasks are automatically saved in the file tasks.json.

## Run tests

From the root folder of the project, run:

python3 -m tests.test_tasks

Tests validate the core task management logic.

## Project structure

task_manager_python/
├── main.py
├── README.md
├── requirements.txt
├── tasks.json
├── task_manager/
│   ├── __init__.py
│   ├── cli.py
│   ├── tasks.py
│   └── storage.py
├── tests/
│   ├── __init__.py
│   └── test_tasks.py
└── .gitignore

## Technologies used

- Python 3
- JSON file storage
- Basic unit testing

## Author

Esteban




































