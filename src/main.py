import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A simple task tracker CLI written in Python"
    )
    initialize_parser(parser)

    args = parser.parse_args()
    match args.command:
        case "add":
            add_task()
        case "update":
            update_task()
        case "delete":
            delete_task()
        case "mark-in-progress":
            mark_task_in_progress()
        case "mark-done":
            mark_task_done()
        case "list":
            list_tasks()


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
                "choises": ["done", "todo", "in-progress"],
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


def add_task():
    pass


def update_task():
    pass


def delete_task():
    pass


def mark_task_in_progress():
    pass


def mark_task_done():
    pass


def list_tasks():
    pass


if __name__ == "__main__":
    main()
