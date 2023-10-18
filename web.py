import streamlit as sl
from functions import get_todos, change_todo
sl.title("MY todo App")
todos = get_todos()
def add_todo():
    newtodo = sl.session_state['new_todo']
    todos.append(newtodo+'\n')
    change_todo(todos)
    sl.session_state['new_todo']=""

for index,todo in enumerate(todos):
   checkbox= sl.checkbox(todo ,key=index)
   if checkbox:
       todos.pop(index)
       change_todo(todos)
       del sl.session_state[index]
       sl.rerun()

sl.text_input(label='', placeholder='enter your todo', on_change=add_todo, key='new_todo')

sl.session_state