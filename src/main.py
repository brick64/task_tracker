import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A simple task tracker CLI written in Python"
    )
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add", help="Add new task")
    add.add_argument(
        "description", type=str, help="A short description of the task", required=True
    )

    update = subparsers.add_parser("update", help="Udate existing task")
    update.add_argument("id", type=int, help="A unique identifier for the task")
    update.add_argument(
        "description", type=str, help="A short description of the task", required=True
    )

    delete = subparsers.add_parser("delete", help="Delete task")
    delete.add_argument("id", type=int, help="A unique identifier for the task")

    mark_in_progreess = subparsers.add_parser(
        "mark-in-progress", help="Mark task in progress"
    )
    mark_in_progreess.add_argument(
        "id", type=int, help="A unique identifier for the task"
    )

    mark_done = subparsers.add_parser("mark-done", help="Mark task done")
    mark_done.add_argument("id", type=int, help="A unique identifier for the task")

    list = subparsers.add_parser("list", help="List existing tasks")
    list.add_argument(
        "status",
        type=str,
        choices=["done", "todo", "in-progress"],
        default="",
        help="The status of the task",
    )


if __name__ == "__main__":
    main()
