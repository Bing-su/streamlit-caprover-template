import streamlit as st


option = st.selectbox("Select one", ["Hello, World!", "foo", "spam"])
d = {"Hello, World!": "Hello, World!", "foo": "bar", "spam": "ham"}

st.title(d[option])
