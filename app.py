import streamlit as st
from functions import *

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EcoTrack",
    page_icon="🌱",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("🌱 EcoTrack: Smart Carbon Footprint Calculator & Analysis System")

st.markdown("""
Estimate your daily carbon footprint based on your lifestyle choices.
This system analyzes your activities and provides an approximate emission score.
""")

# ---------------- INPUT SECTION ----------------
st.header("📊 Enter Your Details")

transport = st.selectbox(
    "🚗 Transportation Type",
    ["Car", "Bike", "Public Transport", "Walking"]
)

distance = st.number_input(
    "📍 Distance traveled per day (in km)",
    min_value=0.0,
    step=1.0
)

electricity = st.number_input(
    "💡 Electricity usage per day (in kWh)",
    min_value=0.0,
    step=0.5
)

diet = st.selectbox(
    "🍽️ Diet Type",
    ["Vegetarian", "Non-Vegetarian", "Vegan"]
)

# ---------------- CALCULATION ----------------
if st.button("Calculate Carbon Footprint"):
    result = calculate_carbon_footprint(
        transport,
        distance,
        electricity,
        diet
    )

    st.success(f"🌍 Your estimated carbon footprint is: {result} kg CO₂/day")

    # ---------------- INTERPRETATION ----------------
    st.subheader("📈 Analysis")

    if result < 5:
        st.info("✅ Low impact lifestyle. Keep it up!")
    elif result < 10:
        st.warning("⚠ Moderate impact. Consider reducing energy usage.")
    else:
        st.error("❌ High impact. Try eco-friendly alternatives.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("© 2026 Varun Jindal | EcoTrack Web App")
