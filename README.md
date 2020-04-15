# MiniTodo

MiniTodo is a very simple CLI to-do list written in Python. 

On running the script, you can enter the following commands:

- *help* or *h* to open user guide
- *view* or *v* to view to-do list
- *add* or *a* to add a new to-do task
- *edit* or *e* to edit a task
- *delete* or *d* to delete a task
- *quit* or *q* to save and quit

All your entries are automatically pickled and saved into tasks_save.data, located in the same directory as to_do.py.

Full feature list:
- Add to-do tasks with a name or description (e.g "Grocery shopping"), and deadline (e.g "tomorrow", "20/02/2020")
- Edit task entries, deadlines, and completion status (Done/Not Done)
- Delete a single task, or all tasks at once
- Store tasks in order of creation
- Automatically load tasks from tasks_save.data (if exists) on running the script
- Automatically save tasks to tasks_save.data (overwriting) when properly exiting the script

Task sorting by deadline is not implemented, because the deadline field can be any possible string. 

Further extensibility/TODO:

Add command line arguments for quicker usage (e.g `python to_do.py -view` or `python to_do.py -delete all`)
