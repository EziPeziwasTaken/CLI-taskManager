import argparse
from task_tool.core import TaskManager

def main():
    parser = argparse.ArgumentParser(description="Task CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")
    add_parser.add_argument("-d", "--description", type=str, default="", help="Task description")
    add_parser.add_argument("-p", "--priority", type=str, default="medium", choices=["low", "medium", "high"])

    subparsers.add_parser("list", help="List tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add":
        task = manager.add_task(args.title, args.description, args.priority)
        print(f"Added: {task.id}. {task.title} ({task.priority})")
    elif args.command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        for t in tasks:
            status = "✔" if t.done else "✗"
            print(f"{t.id}. {t.title} ({t.priority}) - {t.description} [{status}]")
    elif args.command == "done":
        if manager.mark_done(args.id):
            print(f"Task {args.id} marked as done.")
        else:
            print(f"Task {args.id} not found.")
    elif args.command == "delete":
        if manager.delete_task(args.id):
            print(f"Task {args.id} deleted.")
        else:
            print(f"Task {args.id} not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
