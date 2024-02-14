import streamlit as st

with st.expander("See details"):
    st.write("Here's a dynamically created expander.")

num_columns = st.slider("Select number of columns:", 1, 5, 2)
cols = st.columns(num_columns)

for i, col in enumerate(cols):
    col.write(f"Column {i+1}")
    col.button(f"Button {i+1}", key=f"btn_{i}")
