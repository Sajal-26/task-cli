# Task Tracker

Task Tracker is a command-line tool for managing to-do lists, implemented in Python and using JSON for data storage.

Project : [project page](https://roadmap.sh/projects/task-tracker)

## Features

- Add tasks
- Delete tasks
- Update task descriptions
- Update task statuses (todo, in-progress, done)
- List tasks, optionally filtering by status

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Sajal-26/task-cli
    ```
2. Navigate to the project directory:
    ```bash
    cd task-cli
    ```

## Usage

### Python Script

Run the `task-cli.py` script using Python:

```bash
python task-cli.py [command] [arguments]
```

### Batch File

A batch file `task-cli.bat` is provided to run the script easily. Place the `task-cli.bat` file in a directory included in your system's PATH, or specify the full path when calling it.

```bash
task-cli [command] [arguments]
```

### Commands

- `list [status]` - List all tasks or filter by status
- `add [task description]` - Add a new task
- `delete [id]` - Delete a task by its ID
- `update [id] [new description]` - Update the description of a task by its ID
- `mark-in-progress [id]` - Mark a task as in-progress by its ID
- `mark-done [id]` - Mark a task as done by its ID
- `mark-todo [id]` - Mark a task as todo by its ID
- `help` - Show help information

### Examples

- Add a new task:
    ```bash
    task-cli add Buy groceries
    ```

- List all tasks:
    ```bash
    task-cli list
    ```

- List tasks with status "done":
    ```bash
    task-cli list done
    ```

- Update a task description:
    ```bash
    task-cli update 1 Buy groceries and cook dinner
    ```

- Delete a task:
    ```bash
    task-cli delete 1
    ```

- Mark a task as in-progress:
    ```bash
    task-cli mark-in-progress 2
    ```

- Mark a task as done:
    ```bash
    task-cli mark-done 2
    ```
