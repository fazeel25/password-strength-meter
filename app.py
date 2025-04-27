import streamlit as st
import re

# --- Page Config ---
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

# --- Helper function to check password strength ---
def password_strength(password):
    strength = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Password should be at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # Number check
    if re.search(r"\d", password):
        strength += 1
    else:
        suggestions.append("Add numbers (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Add special characters (!, @, #, etc.).")

    return strength, suggestions

# --- UI Start ---
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>🔒 Password Strength Meter</h1>
    """, unsafe_allow_html=True
)

st.write("### Enter your password below:")

password = st.text_input("Password", type="password")

if password:
    strength, suggestions = password_strength(password)

    # Progress bar color
    progress_color = "red"
    if strength == 2 or strength == 3:
        progress_color = "orange"
    elif strength == 4:
        progress_color = "yellow"
    elif strength == 5:
        progress_color = "green"

    # Progress bar UI
    progress_percentage = (strength / 5) * 100
    st.progress(strength/5)

    # Display strength feedback
    if strength <= 2:
        st.error("🔴 Weak Password!")
    elif strength == 3 or strength == 4:
        st.warning("🟡 Medium Strength Password!")
    elif strength == 5:
        st.success("🟢 Strong Password!")

    # Suggestions
    if suggestions:
        st.write("**Suggestions to Improve:**")
        for suggestion in suggestions:
            st.write("- ", suggestion)
else:
    st.info("👆 Start typing your password to see the strength.")

# Footer
st.markdown("<br><hr><center>Made with ❤️ by Faze</center>", unsafe_allow_html=True)
