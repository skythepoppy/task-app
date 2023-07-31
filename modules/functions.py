FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    '''Read a text file and return
    the list of to-do items'''

    with open(filepath, 'r') as file_local:    # uses context manager
        todos_local = file_local.readlines()  # local variable
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    '''Writes specified to-do items
    to the text file'''

    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    # modifies the txt file but it doesn't need to return anything