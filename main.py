import streamlit as st

# Title
st.title("My First Streamlit App")

# Header
st.header("Welcome to Streamlit")

# Text
st.write("Streamlit is an easy-to-use framework for building web apps.")

# Input and Output
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

#Button
if st.button("Click Me"):
    st.write("Button clicked!")

#Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age: {age}")

#File uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.write(f"File uploaded: {uploaded_file.name}")

#Columns
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

#expander
with st.expander("See more details"):
    st.write("Here are the details.")
