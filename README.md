# Codex Task Progress Tracker

This repository provides a simple command line application for managing task progress per user. Tasks are stored locally in `tasks.json`.

## Usage

```
python tasks.py add-user <username>
python tasks.py add-task <username> <task description>
python tasks.py update <username> <task index> <progress percentage>
python tasks.py list <username>
```

Example:

```
python tasks.py add-user alice
python tasks.py add-task alice "Write unit tests"
python tasks.py update alice 0 40
python tasks.py list alice
```
