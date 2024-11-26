def schedule_tasks(task_hierarchy):
    """
    Schedule tasks based on their dependencies and priorities.
    
    :param task_hierarchy: List of tasks, where each task is a dictionary with keys:
                           - id: Unique identifier for the task.
                           - name: Name or description of the task.
                           - subtasks: List of subtasks (nested hierarchy), if any.
                           - priority: Priority level of the task (optional).
    :return: List of scheduled tasks in the order they should be executed.
    """
    scheduled_tasks = []

    def schedule(task):
        # Schedule subtasks first
        if 'subtasks' in task and task['subtasks']:
            for subtask in sorted(task['subtasks'], key=lambda x: x.get('priority', 0), reverse=True):
                schedule(subtask)
        # Schedule the current task
        scheduled_tasks.append(task)

    # Sort the top-level tasks by priority and schedule them
    for task in sorted(task_hierarchy, key=lambda x: x.get('priority', 0), reverse=True):
        schedule(task)

    return scheduled_tasks

# Example test case
task_hierarchy = [
    {
        'id': 1,
        'name': 'Task 1',
        'priority': 2,
        'subtasks': [
            {
                'id': 2,
                'name': 'Subtask 1.1',
                'priority': 1,
                'subtasks': []
            },
            {
                'id': 3,
                'name': 'Subtask 1.2',
                'priority': 3,
                'subtasks': []
            }
        ]
    },
    {
        'id': 4,
        'name': 'Task 2',
        'priority': 1,
        'subtasks': []
    }
]

# Schedule the tasks
scheduled_tasks = schedule_tasks(task_hierarchy)
for task in scheduled_tasks:
    print(f"Task ID: {task['id']}, Name: {task['name']}, Priority: {task.get('priority', 'N/A')}")
