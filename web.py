import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("Manage your tasks with this simple To-Do app.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "Enter a task",
              placeholder = "Add new task",
              on_change=add_todo,
              key='new_todo')