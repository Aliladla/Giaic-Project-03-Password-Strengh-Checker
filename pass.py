import streamlit as st
import re


st.set_page_config(page_title="Password Strengh Checker!!!",page_icon="🔒")

# Initialize variables
st.title("🔒Password Strengh Checker!")

# Display welcome message
st.markdown("""
## Welcome to the ultimate password strengh checker!👋
use this simple tool to check the strengh of your password and get suggestions on how to make it stronger.
        we will give you helpful tips to create  a ** Strong Password **  🔒""")

password = st.text_input("Enter Your Password",type="password")
feedback = []
score = 0

# Check password length
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for upper and lower case letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%&]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (e.g., !@#$%&).")

    # Provide feedback based on score
    if score == 4:
        feedback.append("✅ Your password is strong!😊")
    elif score == 3:
        feedback.append("🟡 Your password has medium strength. It could be stronger.")
    else:
        feedback.append("🔴 Your password is weak. Please make it stronger.")

# Show improvement suggestions or message based on the password input
if feedback:
    st.markdown("## Improvement Suggestions")
    for tip in feedback:
        st.write(tip)
else:
    st.info("Please enter your password to get started.")














