import streamlit as st


option = st.selectbox("Select one", ["Hello, World!", "foo", "spam", "python"])
d = {"Hello, World!": "Hello, World!", "foo": "bar", "spam": "ham", "python": "3.8.10"}

st.title(d[option])
