from tabulate import tabulate
import datetime
import argparse
import json
import os

class TaskTracker:
    '''
        project link: https://roadmap.sh/projects/task-tracker
    '''

    def __init__(self) -> None:
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tasks.json'))
        if not os.path.exists(self.path):
            self.__tasks = []
            with open(self.path, 'w', encoding='UTF-8') as f:
                json.dump(self.__tasks, f, indent=4, ensure_ascii=False)
        else:
            with open(self.path, 'r', encoding='UTF-8') as f:
                self.__tasks = json.load(f)

    def list_task(self, status: str | None = None) -> None:
        '''
            List all tasks or filter by status.

            Args:
                status(str): status to be filtered (optional)
            
            Returns: None
        '''
        headers = ["ID", "Description", "Status", "Created At", "Updated At"]
        table = []
        for i in self.__tasks:
            if status and status != i.get("status"):
                continue
            table.append([
                i.get('id'),
                i.get('description'),
                i.get('status'),
                i.get('createdAt'),
                i.get('updatedAt')
            ])
    
        print(tabulate(table, headers, tablefmt="grid"))

    def add(self, task: str) -> bool:
        '''
            Add a new task.

            Args:
                task (str): task to be added

            Returns:
                bool : added or not added
        '''
        try:
            self.__tasks.append({
                "id": len(self.__tasks) + 1,
                "description": task,
                "status": "todo",
                "createdAt": datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
                "updatedAt": None
            })

            with open(self.path, 'w', encoding='UTF-8') as f:
                json.dump(self.__tasks, f, indent=4, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error adding task: {e}")
            return False

    def update_task(self, id: int, task: str) -> bool:
        '''
            Update the description of a task by its ID.

            Args:
                id (int): id of the task
                task (str) : new task

            Returns:
                bool: updated or not
        '''
        if id > len(self.__tasks) or id <= 0:
            return False
        
        try:
            self.__tasks[id - 1]['description'] = task
            self.__tasks[id - 1]['updatedAt'] = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

            with open(self.path, 'w', encoding='UTF-8') as f:
                json.dump(self.__tasks, f, indent=4, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Error updating task: {e}")
            return False

    def update_status(self, id: int, status: str) -> bool:
        '''
            Update the status of a task by its ID.

            Args:
                id (int): id of the task
                status (str): status of the task

            Returns:
                bool: updated or not
        '''
        if id > len(self.__tasks) or id <= 0:
            return False
        
        try:
            self.__tasks[id - 1]['status'] = status
            self.__tasks[id - 1]['updatedAt'] = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

            with open(self.path, 'w', encoding='UTF-8') as f:
                json.dump(self.__tasks, f, indent=4, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Error updating status: {e}")
            return False

    def delete(self, id: int) -> bool:
        '''
            Delete a task by its ID.

            Args:
                id (int): id of the task
            
            Returns:
                bool: deleted or not
        '''
        if id > len(self.__tasks) or id <= 0:
            return False
        
        try:
            self.__tasks.pop(id - 1)

            for index, task in enumerate(self.__tasks):
                task['id'] = index + 1

            with open(self.path, 'w', encoding='UTF-8') as f:
                json.dump(self.__tasks, f, indent=4, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Error deleting task: {e}")
            return False

def args() -> str:
    '''
        Parse command-line arguments.

        Args:
            None

        Returns:
            str : arguments
    '''
    parser = argparse.ArgumentParser(description="todo list commands")
    parser.add_argument("arg", type=str, nargs='*', help="CLI for todo list")
    argument = parser.parse_args()
    return argument.arg

if __name__ == "__main__":
    t = TaskTracker()

    argument = args()

    if len(argument) == 0:
        print("Please enter any command")
        exit()

    command = argument[0]
    if command == "add":
        try:
            task = " ".join(argument[1:])
        except:
            print("Please enter the task!!")
            exit()
        
        feedback = t.add(task=task)
        if feedback:
            print("Task added successfully!")
        else:
            print("Task was not added!")

    elif command == "delete":
        try:
            id = int(argument[1])
        except:
            print("Please enter the task id!")
            exit()

        feedback = t.delete(id=id)
        if feedback:
            print("Task deleted successfully!")
        else:
            print("Task was not deleted!")

    elif command == "update":
        try:
            id = int(argument[1])
            task = " ".join(argument[2:])
        except:
            print("Not enough parameters!")
            exit()

        feedback = t.update_task(id=id, task=task)
        if feedback:
            print("Task updated successfully!")
        else:
            print("Task was not updated!")

    elif command == "list":
        if len(argument) == 1:
            t.list_task()
        else:
            t.list_task(status=argument[1])

    elif command == "mark-in-progress":
        try:
            id = int(argument[1])
        except:
            print("Please enter the id!")
            exit()

        feedback = t.update_status(id=id, status="in-progress")
        if feedback:
            print("Status updated successfully")
        else:
            print("Status not updated!")

    elif command == "mark-done":
        try:
            id = int(argument[1])
        except:
            print("Please enter the id!")
            exit()

        feedback = t.update_status(id=id, status="done")
        if feedback:
            print("Status updated successfully")
        else:
            print("Status not updated!")

    elif command == "mark-todo":
        try:
            id = int(argument[1])
        except:
            print("Please enter the id!")
            exit()

        feedback = t.update_status(id=id, status="todo")
        if feedback:
            print("Status updated successfully")
        else:
            print("Status not updated!")

    elif command == "help":
        print("This is a TODO list.")
        print("Options : ")
        print("1. list             - This will list all the todo tasks")
        print("2. add              - This will add a task to the todo list")
        print("3. delete           - This will delete a specific task by their id")
        print("4. update           - This will update the task of a specific id")
        print("5. mark-in-progress - This will mark a task in progress for a specific id")
        print("6. mark-done        - This will mark the task as done for a specific id")
        print("7. mark-todo        - This will mark the task as todo for a specific id")

    else:
        print("You entered the wrong command, please use 'task-cli help' for the commands")
