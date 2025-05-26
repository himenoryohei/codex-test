import argparse
import json
from typing import Dict, List

DATA_FILE = 'tasks.json'

def load_data() -> Dict[str, List[dict]]:
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data: Dict[str, List[dict]]):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_user(data, username: str):
    if username not in data:
        data[username] = []
        print(f"User '{username}' added")
    else:
        print(f"User '{username}' already exists")


def add_task(data, username: str, task: str):
    if username not in data:
        print(f"User '{username}' does not exist")
        return
    data[username].append({'task': task, 'progress': 0})
    print(f"Task added for {username}: {task}")


def update_progress(data, username: str, index: int, progress: int):
    if username not in data:
        print(f"User '{username}' does not exist")
        return
    try:
        data[username][index]['progress'] = progress
        print(f"Updated task {index} for {username} to {progress}%")
    except IndexError:
        print(f"Task index {index} does not exist for {username}")


def list_tasks(data, username: str):
    if username not in data:
        print(f"User '{username}' does not exist")
        return
    for i, t in enumerate(data[username]):
        print(f"{i}: {t['task']} - {t['progress']}%")


def main():
    parser = argparse.ArgumentParser(description='Manage task progress per user')
    subparsers = parser.add_subparsers(dest='command')

    parser_user = subparsers.add_parser('add-user')
    parser_user.add_argument('username')

    parser_add = subparsers.add_parser('add-task')
    parser_add.add_argument('username')
    parser_add.add_argument('task')

    parser_update = subparsers.add_parser('update')
    parser_update.add_argument('username')
    parser_update.add_argument('index', type=int)
    parser_update.add_argument('progress', type=int)

    parser_list = subparsers.add_parser('list')
    parser_list.add_argument('username')

    args = parser.parse_args()
    data = load_data()

    if args.command == 'add-user':
        add_user(data, args.username)
    elif args.command == 'add-task':
        add_task(data, args.username, args.task)
    elif args.command == 'update':
        update_progress(data, args.username, args.index, args.progress)
    elif args.command == 'list':
        list_tasks(data, args.username)
    else:
        parser.print_help()
        return

    save_data(data)

if __name__ == '__main__':
    main()
