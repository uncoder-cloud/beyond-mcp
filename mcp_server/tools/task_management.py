tasks = []

def create_task(name, description):
    task = {"name": name, "description": description, "status": "open"}
    tasks.append(task)
    return "Task created"

def list_tasks():
    if not tasks:
        return "No tasks found"
    task_list = ""
    for task in tasks:
        task_list += f"{task['name']}: {task['description']} ({task['status']})\n"
    return task_list

def update_task_status(name, status):
    for task in tasks:
        if task["name"] == name:
            task["status"] = status
            return "Task status updated"
    return "Task not found"
