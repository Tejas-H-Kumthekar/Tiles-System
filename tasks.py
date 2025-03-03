tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added!"

def view_tasks():
    if not tasks:
        return "No tasks available."
    return "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        return f"Task '{removed}' deleted!"
    except IndexError:
        return "Invalid task number!"
