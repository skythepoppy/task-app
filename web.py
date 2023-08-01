import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("Manage your tasks with this simple To-Do app.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "Enter a task",
              placeholder = "Add new task")