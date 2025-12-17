# Todo List Application

A simple command-line todo list manager built with Python that helps you organize and track your tasks with priority levels.

## Features

- **Add Tasks** - Create new tasks with descriptions and priority levels (High, Medium, Low)
- **View Tasks** - Display all tasks sorted by priority with completion status
- **Mark as Done** - Mark tasks as completed
- **Edit Tasks** - Update task descriptions and priorities
- **Delete Tasks** - Remove tasks from your list
- **Persistent Storage** - Tasks are saved to a JSON file and persist between sessions

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## Installation

1. Download or clone the repository
2. Ensure you have Python 3 installed on your system
3. No additional installation required!

## Usage

Run the application from your terminal:

```bash
python tasks.py
```

### Menu Options

When you run the application, you'll see a menu with the following options:

1. **Add Task** - Enter a task description and select a priority level
2. **View Tasks** - See all your tasks sorted by priority (High → Medium → Low)
3. **Mark Task as Done** - Mark a task as completed
4. **Edit Task** - Modify the description or priority of an existing task
5. **Delete Task** - Remove a task from your list
6. **Exit** - Close the application

### Task Priority Levels

- **High** - Urgent or important tasks
- **Medium** - Regular priority tasks (default)
- **Low** - Tasks that can be done later

## Data Storage

Tasks are automatically saved to `tasks.json` in the same directory as the script. The file is created automatically when you add your first task.

## Example Workflow

```
1. Add Task → "Complete Python project" → Priority: High
2. Add Task → "Buy groceries" → Priority: Medium
3. View Tasks → See your organized list
4. Mark Task as Done → Select task #1
5. View Tasks → See updated completion status
```

## File Structure

```
.
├── tasks.py       # Main application file
└── tasks.json     # Auto-generated task storage (created on first use)
```

## Notes

- Task descriptions cannot be empty
- Task numbers are displayed based on priority sort order
- Both `done` and `completed` fields are supported for backward compatibility
- Invalid inputs are handled gracefully with error messages

## License

This project is open source and available for educational purposes.

## Author

Created as a Python mini project.