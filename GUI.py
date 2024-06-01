import streamlit as st
import functions

todos = functions.readList()
def func():
    todo = st.session_state["mykey"]
    todos.append(todo+"\n")
    functions.writeList(todos)
    st.session_state["mykey"] = ""
st.title("This is Mytodoapp")
st.subheader("this is subheader")


# i = 5
# while i<= 5:
#     st.checkbox("please click here")
#     i+=1

st.text_input(label ="Enter a todo", placeholder="enter a todo",on_change=func,key ="mykey")




for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.writeList(todos)
        del st.session_state[f"{todo}_{index}"]
        st.experimental_rerun()


# st.session_state

