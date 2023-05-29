import streamlit as st
import modules.functions as mf

todos = mf.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    mf.update_todos(todos)
    st.session_state["new_todo"] = ""


st.title("To-Do App")
st.subheader("Put your plans in order!")
st.write("With this App you will increase your productivity.")

for index, todo in enumerate(todos):
    chkbox = st.checkbox(todo, key=todo)
    if chkbox:
        todos.pop(index)
        mf.update_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a to-do...",
              on_change=add_todo, key='new_todo')


# st.session_state