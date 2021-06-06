import streamlit as st


option = st.selectbox("Select one", ["Hello, World!", "foo", "ham"])
d = {"Hello, World!": "Hello, World!", "foo": "bar", "ham": "spam"}

st.title(d[option])
