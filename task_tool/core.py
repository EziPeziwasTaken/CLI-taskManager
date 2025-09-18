from typing import List
from task_tool.models import Task
from task_tool.storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = load_tasks()

    def _next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, title: str, description: str, priority: str) -> Task:
        new_task = Task(
            id=self._next_id(),
            title=title,
            description=description,
            priority=priority
        )
        self.tasks.append(new_task)
        save_tasks(self.tasks)
        return new_task

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def mark_done(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                save_tasks(self.tasks)
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                save_tasks(self.tasks)
                return True
        return False
