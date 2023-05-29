import streamlit as st
import modules.functions as mf

todos = mf.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    mf.update_todos(todos)


st.title("To-Do App")
st.subheader("Put your plans in order!")
st.write("With this App you will increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a to-do...",
              on_change=add_todo, key='new_todo')
