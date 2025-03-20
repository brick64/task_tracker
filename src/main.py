import argparse
import json
from datetime import datetime, timezone


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A simple task tracker CLI written in Python"
    )
    initialize_parser(parser)

    args = parser.parse_args()
    match args.command:
        case "add":
            add_task(description=args.description)
        case "update":
            update_task(id=args.id, description=args.description)
        case "delete":
            delete_task(id=args.id)
        case "mark-in-progress":
            mark_task_in_progress(id=args.id)
        case "mark-done":
            mark_task_done(id=args.id)
        case "list":
            list_tasks(status=args.status)


def initialize_parser(parser: argparse.ArgumentParser) -> None:
    commands = {
        "add": {
            "help": "Add new task",
            "description": {
                "type": str,
                "help": "A short description of the task",
            },
        },
        "update": {
            "help": "Udate existing task",
            "id": {"type": int, "help": "A unique identifier for the task"},
            "description": {
                "type": str,
                "help": "A short description of the task",
            },
        },
        "delete": {
            "help": "Delete task",
            "id": {"type": int, "help": "A unique identifier for the task"},
        },
        "mark-in-progress": {
            "help": "Mark task in progress",
            "id": {"type": int, "help": "A unique identifier for the task"},
        },
        "mark-done": {
            "help": "Mark task done",
            "id": {"type": int, "help": "A unique identifier for the task"},
        },
        "list": {
            "help": "List existing tasks",
            "status": {
                "type": str,
                "choises": ["done", "todo", "in-progress", ""],
                "default": "",
                "help": "The status of the task",
            },
        },
    }

    subparsers = parser.add_subparsers(dest="command")

    for command in commands:
        parser_details = commands[command]
        help = parser_details.pop("help")
        subparser = subparsers.add_parser(command, help=help)
        for arg in parser_details:
            arg_details = parser_details[arg]
            type = arg_details.pop("type")
            help = arg_details.pop("help")
            choises = arg_details.pop("choises") if "choises" in arg_details else None
            default = arg_details.pop("default") if "default" in arg_details else None
            subparser.add_argument(
                arg, type=type, choices=choises, default=default, help=help
            )


def add_task(description: str):
    data = read_db()
    tasks = data["tasks"]
    ids = list(map(int, tasks.keys()))
    id = max(ids) + 1 if ids else 0
    task = {
        "description": description,
        "status": "todo",
        "createdAt": str(datetime.now(timezone.utc)),
        "updatedAt": str(datetime.now(timezone.utc)),
    }
    data["tasks"][id] = task
    write_db(data=data)


def update_task(id: int, description: str):
    data = read_db()
    task = data["tasks"][str(id)]
    task["description"] = description
    task["updatedAt"] = str(datetime.now(timezone.utc))
    write_db(data=data)


def delete_task(id: int):
    data = read_db()
    tasks = data["tasks"]
    tasks.pop(str(id))
    write_db(data=data)


def mark_task_in_progress(id: int):
    data = read_db()
    task = data["tasks"][str(id)]
    task["status"] = "in-progress"
    write_db(data=data)


def mark_task_done(id: int):
    data = read_db()
    task = data["tasks"][str(id)]
    task["status"] = "done"
    write_db(data=data)


def list_tasks(status: str):
    data = read_db()
    if status == "":
        tasks = list(data["tasks"].items())
    else:
        tasks = [i for i in list(data["tasks"].items()) if i[1]["status"] == status]

    for task in tasks:
        print(
            "-----------------------------------------\n"
            f"Id:           {task[0]}\n"
            f"Description:  {task[1]['description']}\n"
            f"Status:       {task[1]['status']}\n"
            f"Created At:   {task[1]['createdAt']}\n"
            f"Updated At:   {task[1]['updatedAt']}\n",
            end="",
        )
    print("-----------------------------------------\n", end="")


def init_db():
    with open("db.json", "w") as outfile:
        data = {"tasks": {}}
        json.dump(data, outfile)
        return data


def read_db():
    try:
        with open("db.json", "r") as db:
            data = json.load(db)
    except FileNotFoundError:
        data = init_db()

    return data


def write_db(data):
    with open("db.json", "w") as db:
        json.dump(data, db)


if __name__ == "__main__":
    main()
