filepath = 'todos.txt'
def get_todos(pathname=filepath):
    with open(pathname, 'r') as file_local:
        todos = file_local.readlines()
    return todos

def change_todo(todosUpdate ,pathanme =filepath):
    with open(pathanme, 'w') as file_local:
        file_local.writelines(todosUpdate)