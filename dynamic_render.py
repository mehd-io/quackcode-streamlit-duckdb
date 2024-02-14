import streamlit as st

# User selects the type of component they want to display
component_type = st.selectbox('Choose a component to display:', 
                              ['Text', 'Button', 'Slider'])

if component_type == 'Text':
    # Dynamically display a text input
    user_input = st.text_input("Enter some text")
    st.write(f"You entered: {user_input}")

elif component_type == 'Button':
    # Dynamically display a button
    if st.button('Click Me!'):
        st.success("Button was clicked!")

elif component_type == 'Slider':
    # Dynamically display a slider
    slider_value = st.slider("Choose a number", min_value=0, max_value=100)
    st.write(f"Slider value: {slider_value}")
