def add_task(task_name):
	"""Adds a new task to the task list."""
	global TASKS
	TASKS.append(task_name)
	print(f"Task added: {task_name}")
TASKS = [] # Global task list
print("Project Utility V1.1 - Task Manager Initialized")
# Testing the new feature
add_task("Review CI/CD Pipeline")
add_task("Write Documentation")
print(f"Current Tasks: {TASKS}")
