import streamlit as st

#custom css for enhanced UI(UI ko behtr bnane k lie custom styling)
st.markdown(
    """"
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px; 
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton<button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black
     }
     .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        color: #00c9ff;
        border-radius: 10px;
        marging: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
        }
        .footer {
        text-align: center;
        maging-top: 50px;
        font-size: 14px;
        color:black
        }
        </style>
    """,
    unsafe_allow_html=True
)

#title and description:(title aur chota sa intro)
st.markdown("<h1>🚀 Universal Unit Convertor</hi>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight and Temperature.")

# sidebar menu(conversion type select krne ka option)
conversion_type=st.sidebar.selectbox("Choose Conversion Type", ["Length","Weight","Temperature"])

# input value (user se value lene k lie)
value=st.number_input("Enter Value",value=0.0,min_value=0.0,step=0.1)

# layout for unit selection(from or to unit select krne k lie setup)
col1, col2 = st.columns(2)



if conversion_type == "length":
        with col1:
            from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Miles", "Inches", "Feet", "Yards", 'Millimeters'])
        with col2:
            to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Miles", "Inches", "Feet", "Yards", 'Millimeters'])
elif conversion_type == "weight":
        with col1:
            from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
        with col2:
            to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temprature":
        with col1:
            from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])



# converter function( alg alg conversion functions k lie)
def length_converter(value, from_unit, to_unit):
    # length units ko conversion factor k zariye convert krna 
    length_units =  {  
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,   
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches':39.3701
    }
    return (value / length_units [from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    # weight units ko conversion factor k zariye convert krna
    weight_units = {
         'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    # Temperature conversion logic
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value -32) *9/5 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value -273.15 if to_unit == "Celsius" else (value -273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value



#button for conversion
if st.button("🤖Convert"):
    if conversion_type == "Length":
         result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
         result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
         result = temp_converter(value, from_unit, to_unit)

    # result ko dikhana (conversion ka result show krna)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# footer (neeche footer message)
st.markdown("<div class='footer'>Created with 💖 by Usama Sharif </div>",unsafe_allow_html=True) 
    




    



      
    


