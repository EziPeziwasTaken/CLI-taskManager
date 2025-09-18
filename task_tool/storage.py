import json
from pathlib import Path
from typing import List
from task_tool.models import Task

FILE_PATH = Path("tasks.json")

def load_tasks() -> List[Task]:
    if FILE_PATH.exists():
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task(**item) for item in data]
    return []

def save_tasks(tasks: List[Task]) -> None:
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([t.dict() for t in tasks], f, ensure_ascii=False, indent=2)
