#!/usr/bin/env python3

# simple object-oriented to do list program
# chants-de-maldoror on github

import pickle


class Entry:
    def __init__(self):
        self.name = ""
        self.deadline = ""
        self.completed = False

    def get_name(self):
        return self.name

    def get_deadline(self):
        return self.deadline

    def get_completed(self):
        return self.completed

    def set_name(self):
        # enable user to edit to-do list entry
        new_name_input = ""
        while new_name_input == "":  # while loop to make sure user actually inputs something
            new_name_input = input("Set new name:\n")
            self.name = new_name_input

    def set_deadline(self):
        self.deadline = input("Set new deadline:\n")

    def set_completed(self):

        user_input_completed = None

        while user_input_completed is None:

            user_input = input("Set completion status, True/False:\n")

            if user_input.lower() == "true" or user_input.lower() == "t":
                user_input_completed = True

            elif user_input.lower() == "false" or user_input.lower() == "f":
                user_input_completed = False

            else:
                print("Please enter True or False.")

            self.completed = user_input_completed


class EntriesList:
    # save the entries list as an object, so we can define custom functions
    def __init__(self):
        self.tasks_list = []

    def add_task(self):
        new_task = Entry()
        user_name_input = None
        while user_name_input is None:
            user_name_input = input("Enter task name, do not leave blank:\n")
            new_task.name = user_name_input
        new_task.deadline = input("Enter task deadline, or leave blank:\n")
        new_task.completed = False
        self.tasks_list.append(new_task)

    def get_task(self, index):
        # return the object at a given index of the list
        try:
            for i, entry in enumerate(self.tasks_list):
                if 0 <= index <= len(self.tasks_list):
                    if i == index:
                        return entry
                    else:
                        continue
                else:
                    print("Could not find that entry.")
        except ValueError:
            print("Please enter an integer.")

    def format_task(self, index):
        # tedious formatting for task view
        try:
            for i, entry in enumerate(self.tasks_list):
                if 0 <= index <= len(self.tasks_list):
                    if i == index:
                        if entry.get_deadline() != "":
                            if not entry.get_completed(): # indexes are plus one for more natural counting
                                return "[{0}] {1} -- {2} -- Not done!".format(index + 1, entry.get_name(),
                                                                              entry.get_deadline())
                            else:
                                return "[{0}] {1} -- {2} -- Done!".format(index + 1, entry.get_name(),
                                                                          entry.get_deadline())
                        else:
                            if not entry.get_completed():
                                return "[{0}] {1} -- Not done!".format(index + 1, entry.get_name())
                            else:
                                return "[{0}] {1} -- Done!".format(index + 1, entry.get_name())
                    else:
                        continue
                else:
                    # this won't happen
                    print("Could not find that entry.")

        except ValueError:
            print("Please enter an integer.")

    def list_tasks(self):
        # simply print the tasks, passed through the formatting function above
        if len(self.tasks_list) != 0:
            for index, tasks in enumerate(self.tasks_list):
                print(self.format_task(index))
            return True
        else:
            print("You have no tasks.")
            return None


if __name__ == "__main__":

    all_tasks = EntriesList()

    try:
        loadfile = './tasks_save.data'
        with open(loadfile, 'rb') as pickle_file:

            all_tasks.tasks_list = pickle.load(pickle_file)

    except FileNotFoundError or EOFError:
        print("Could not find tasks_save.data. If this is NOT your first time\n"
              "running this program, make sure that file is in the same directory.\n")

    print("Welcome to your to do list. Type help for a list of commands.")

    running = True
    while running:

        menu = input()

        # show commands
        if menu.lower() == "help" or menu.lower() == "h":
            print("\n--- USER GUIDE ---\n"
                  "this menu: help or h\n"
                  "view tasks: v\n"
                  "add new task: a\n"
                  "edit task: e\n"
                  "delete task(s): d\n"
                  "save & quit: q\n\n"
                  "a note on saving and loading: tasks are automatically loaded\n"
                  "from tasks_save.txt on start if file exists in the same directory.\n"
                  "saving is only performed when you quit using the above command.\n"
                  "--- --- -- --- ---\n")

        # list all tasks
        elif menu.lower() == "v":
            all_tasks.list_tasks()

        # adding an entry
        elif menu.lower() == "a":
            all_tasks.add_task()
            print("Task added.")

        # deleting entries
        elif menu.lower() == "d":
            # go back to menu if user has no tasks in list
            if all_tasks.list_tasks() is None:
                continue

            # figure out the task to delete, delete that task
            task_to_delete = None
            while task_to_delete is None:
                try:
                    delete_input = input("Please enter the number of the task to delete.\nOr enter 'all' "
                                         "to delete all tasks.\n")
                    if delete_input.isdigit():
                        task_to_delete = all_tasks.get_task(int(delete_input) - 1)  # minus one because we did plus one
                        print("Deleting:", all_tasks.format_task(int(delete_input) - 1))
                        for entry in all_tasks.tasks_list:
                            if entry == task_to_delete:
                                all_tasks.tasks_list.pop(int(delete_input) - 1)
                                del entry
                            else:
                                continue

                    # delete all tasks
                    elif delete_input.lower() == "all":
                        print("Deleting all tasks.")
                        for i, entry in enumerate(all_tasks.tasks_list):
                            del entry
                        all_tasks.tasks_list = []
                        break

                    else:
                        print("Please enter a valid number or delete all.")

                except Exception as e:
                    print(e, "\n Error occurred when deleting.")

        # editing an entry
        elif menu.lower() == 'e':

            # go back to menu if user has no tasks in list
            if all_tasks.list_tasks() is None:
                continue

            # figure out the task to edit, get that task
            task_to_edit = None
            while task_to_edit is None:
                try:
                    which_task = input("Please enter the number of the task to edit.\n")
                    task_to_edit = all_tasks.get_task(int(which_task) - 1)
                    print("Selection:", all_tasks.format_task(int(which_task) - 1))
                except ValueError:
                    print("Please enter a valid number.")

            # actual editing part
            editing = True
            while editing:
                editing_choice = input("What would you like to edit? name (n), deadline (d), or "
                                       "completion status? (c)\nEnter any other key to finish editing.\n")
                if editing_choice.lower() == "n":
                    task_to_edit.set_name()
                    print(all_tasks.format_task(int(which_task) - 1))
                elif editing_choice.lower() == "d":
                    task_to_edit.set_deadline()
                    print(all_tasks.format_task(int(which_task) - 1))
                elif editing_choice.lower() == "c":
                    task_to_edit.set_completed()
                    print(all_tasks.format_task(int(which_task) - 1))
                else:
                    editing = False
                    print("Finished editing.")

        # save and quit
        elif menu.format() == 'q':

            open('./tasks_save.data', 'wb').close()
            savefile = './tasks_save.data'

            with open(savefile, 'wb') as pickle_file:
                pickle.dump(all_tasks.tasks_list, pickle_file)

            running = False
            print("Saved. Goodbye!")

        elif menu.lower() == "hello":
            print("Hello!")

        # catch unrecognised commands
        else:
            print(menu, "is not a recognised command. Type help or h to bring up list of legal commands.")



