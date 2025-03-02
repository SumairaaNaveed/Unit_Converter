import streamlit as st

# Title of the app with emoji
st.title("🌟 Unit Converter App 🌟")

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

# Header for the conversion section with emojis
st.write("## 🔄 Convert between different units of length 🧳")

# 1) Dropdown for 'From' unit with emoji
from_unit = st.selectbox("📐 Select the unit to convert from:", units)

# 2) Dropdown for 'To' unit with emoji
to_unit = st.selectbox("🔄 Select the unit to convert to:", units)

# Input field for the value to be converted
value = st.number_input("📝 Enter the value to convert:", min_value=0.0, value=1.0)

# Adding a little spacing for UI enhancement
st.write("---")

# Conversion and calculation logic
if st.button("🔁 Convert"):
    # Convert the input value to meters
    value_in_meters = value * to_meters[from_unit]
    
    # Convert the meters value to the target unit
    converted_value = value_in_meters / to_meters[to_unit]

    # Display the result in a nice format with emojis
    st.success(f"🎉 {value} {from_unit} = {converted_value:.2f} {to_unit} 🎉")

# Custom CSS styling for the app (centered title and inputs)
st.markdown("""
    <style>
    .css-1d391kg {
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stNumberInput input {
        border-radius: 8px;
    }
    .stSelectbox>div>div>input {
        border-radius: 8px;
    }
    .stTextInput>div>input {
        border-radius: 8px;
    }
    .stSuccess {
        background-color: #d4edda;
        border-color: #c3e6cb;
        color: #155724;
    }
    </style>
    """, unsafe_allow_html=True)

