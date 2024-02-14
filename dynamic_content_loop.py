import streamlit as st

# Example: Generate a dynamic number of text inputs based on user selection
num_inputs = st.number_input(
    "How many fields do you want?", min_value=1, max_value=10, value=1
)

inputs = []
for i in range(int(num_inputs)):
    user_input = st.text_input(f"Input {i+1}", key=f"input_{i}")
    inputs.append(user_input)

if st.button("Submit"):
    st.write("You entered:", inputs)
