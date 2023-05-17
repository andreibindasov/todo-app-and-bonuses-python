"""
This app is developed to revise or perfect basic Python skills
and features
"""

import os.path
import time
from modules.functions import get_todos, update_todos

time.strftime("%d - %m - %Y")
now = time.strftime("%b %d, %Y, %H:%M:%S")
print(now)
user_prompt = "Type 'add' / 'show' / 'edit' / 'complete' / 'exit' : "

todos_f = "todos.txt"
todos = []

text = """
    The term "law" derives from the word "lie" which would mean
    "that which lies" that is "fixed"
"""

while True:
    user_action = input(user_prompt) + "\n"

    if os.path.isfile(todos_f):
        todos = get_todos()

    if user_action.startswith('add'):
        todo = user_action[4:].strip().capitalize() + "\n"
        todos.append(todo)

        update_todos(todos_f, todos)

    elif user_action.startswith('show'):
        if len(todos) != 0:
            # REMOVING EXTRA BLANK ROW ##
            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            #########
            # LIST COMPREHENSION ####
            new_todos = [item.strip('\n') for item in todos]
            #########

            for i, todo in enumerate(todos):
                todo = todo.strip('\n')
                # row = f"{i + 1} - {todo}"
                print(f"{i + 1} - {todo}")

            print(f"Todos length is {i + 1}")

    elif user_action.startswith('edit'):
        try:
            if len(todos) != 0:
                number = int(input("Type the number of Todo to edit: ").strip())
                todos[number - 1] = input(
                    "Type new Todo instead of " + todos[number - 1].upper() + " and press <ENTER>: ") \
                                        .capitalize().strip() + '\n'

                update_todos(todos_f, todos)
        # ValueError, IndexError
        except IndexError:
            print("No item with that index!")
            continue

    elif user_action.startswith('complete'):
        try:
            if len(todos) != 0:
                number = int(input("Type the number of Todo to REMOVE: ").strip())
                todo_c = todos[number - 1].strip('\n ')
                # todos.remove(todos[number-1])
                todos.pop(number - 1)

                update_todos(todos_f, todos)

                print(f"{todo_c} has been removed!")
        except IndexError:
            print("No item with that number!")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("wrong input...")
