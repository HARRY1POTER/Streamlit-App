# import streamlit as st

# # Title of the app
# st.title("BMI Calculator")

# # Input: Weight in kilograms
# weight = st.number_input("Enter your weight (kg):",
#                          min_value=0.0, format="%.2f")

# # Input: Height format selection
# height_unit = st.radio("Select your height unit:", [
#                        'Centimeters', 'Meters', 'Feet'])

# # Input: Height value based on selected unit
# height = st.number_input(
#     f"Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f")

# # Calculate BMI when button is pressed
# if st.button("Calculate BMI"):
#     try:
#         # Convert height to meters based on selected unit
#         if height_unit == 'Centimeters':
#             height_m = height / 100
#         elif height_unit == 'Feet':
#             height_m = height / 3.28
#         else:
#             height_m = height

#         # Prevent division by zero
#         if height_m <= 0:
#             st.error("Height must be greater than zero.")
#         else:
#             bmi = weight / (height_m ** 2)
#             st.success(f"Your BMI is {bmi:.2f}")

#             # BMI interpretation
#             if bmi < 16:
#                 st.error("You are Extremely Underweight")
#             elif 16 <= bmi < 18.5:
#                 st.warning("You are Underweight")
#             elif 18.5 <= bmi < 25:
#                 st.success("You are Healthy")
#             elif 25 <= bmi < 30:
#                 st.warning("You are Overweight")
#             else:
#                 st.error("You are Extremely Overweight")
#     except:
#         st.error("Please enter valid numeric values.")


import streamlit as st

# Page config
st.set_page_config(page_title="BMI Calculator",
                   page_icon="⚖️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 16px;
        }
        .result-box {
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>⚖️ BMI Calculator</h1>",
            unsafe_allow_html=True)
st.write("### Enter your details below:")

# Layout using columns
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("⚖️ Weight (kg)", min_value=0.0, format="%.2f")

with col2:
    height_unit = st.selectbox(
        "📏 Height Unit", ['Centimeters', 'Meters', 'Feet'])

height = st.number_input(
    f"📐 Height ({height_unit.lower()})", min_value=0.0, format="%.2f")

# Button
if st.button("Calculate BMI 🚀"):
    try:
        if height_unit == 'Centimeters':
            height_m = height / 100
        elif height_unit == 'Feet':
            height_m = height / 3.28
        else:
            height_m = height

        if height_m <= 0:
            st.error("⚠️ Height must be greater than zero.")
        else:
            bmi = weight / (height_m ** 2)

            # BMI category + color
            if bmi < 16:
                category = "Extremely Underweight"
                color = "#ff4d4d"
            elif bmi < 18.5:
                category = "Underweight"
                color = "#ffa64d"
            elif bmi < 25:
                category = "Healthy"
                color = "#4CAF50"
            elif bmi < 30:
                category = "Overweight"
                color = "#ff944d"
            else:
                category = "Extremely Overweight"
                color = "#ff4d4d"

            # Display result in styled box
            st.markdown(f"""
                <div class="result-box" style="background-color:{color}; color:white;">
                    <h2>Your BMI: {bmi:.2f}</h2>
                    <p>{category}</p>
                </div>
            """, unsafe_allow_html=True)

            # Progress bar (visual indicator)
            progress = min(int(bmi * 3), 100)
            st.progress(progress)

    except:
        st.error("❌ Please enter valid numeric values.")
