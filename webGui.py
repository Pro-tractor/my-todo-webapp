import streamlit as st
import functions

todos = functions.read_file()


def add_todo():
    todo = st.session_state['new_todo']
    if todo:
        todos.append(todo + "\n")
        functions.write_file(todos)
        st.session_state['new_todo'] = ""


st.title("To-Do App")
st.write("This app was designed to increase your productivity!")

st.text_input(label="", placeholder="Add new todo...", key='new_todo', on_change=add_todo)


for todo in todos:

    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.remove(todo)
        functions.write_file(todos)
        del st.session_state[todo]
        st.rerun()


