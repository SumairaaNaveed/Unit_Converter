import streamlit as st

# Title of the app
st.title("Unit Converter App")

# Conversion dictionary for different units to meters
to_meters = {
    "meters": 1.0,
    "kilometers": 1000.0,
    "miles": 1609.34,
    "foot": 0.3048,
    "yard": 0.9144,
}

# List of available units for selection
units = list(to_meters.keys())

# Header for the conversion section
st.write("## Convert between different units of length")

# 1) Dropdown for 'From' unit
from_unit = st.selectbox("Select the unit to convert from:", units)

# 2) Dropdown for 'To' unit
to_unit = st.selectbox("Select the unit to convert to:", units)

# Input field for the value to be converted
value = st.number_input("Enter the value to convert:", min_value=0.0, value=1.0)

# Adding a little spacing for UI enhancement
st.write("---")

# Conversion and calculation logic
if st.button("Convert"):
    # Convert the input value to meters
    value_in_meters = value * to_meters[from_unit]
    
    # Convert the meters value to the target unit
    converted_value = value_in_meters / to_meters[to_unit]

    # Display the result in a nice format
    st.success(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")

# Adding some styling for the app title and UI elements
st.markdown("""
    <style>
    .css-1d391kg {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
