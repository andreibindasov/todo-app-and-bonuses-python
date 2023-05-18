def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as f:
        todos_list = f.readlines()
    return todos_list


# non-default parameters come before default ones !!!
def update_todos(todos_args, filepath="todos.txt"):
    with open(filepath, 'w') as f:
        f.writelines(todos_args)


if __name__ == "__main__":
    print("hello from functions")
