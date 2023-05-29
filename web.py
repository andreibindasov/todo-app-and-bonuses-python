import streamlit as st
import modules.functions as mf

todos = mf.get_todos()

st.title("To-Do App")
st.subheader("Put your plans in order!")
st.write("With this App you will increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a to-do...")