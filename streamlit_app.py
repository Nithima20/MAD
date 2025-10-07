import streamlit as st
import datetime

# Page title and header
st.set_page_config(page_title="CKCET Canteen Pre-Order", page_icon="🏫🍽️", layout="centered")
st.title("CKCET Canteen Pre-Order App")

# Weekly menu dictionary
weekly_menu = {
    "Monday": "Sambar",
    "Tuesday": "Tomato Rice",
    "Wednesday": "Chicken",
    "Thursday": "Brinjal",
    "Friday": "Lemon Rice",
    "Saturday": "Curd Rice",
}

st.write("### This Week's Menu:")
for day, item in weekly_menu.items():
    st.write(f"**{day}:** {item}")

# User inputs
department = st.text_input("Enter your Department:")
year = st.selectbox("Select your Year:", options=["1st Year", "2nd Year", "3rd Year", "Final Year"])

# Auto-set fooding time based on year
if year in ["1st Year", "Final Year"]:
    fooding_time = "12:15 PM"
else:
    fooding_time = "1:00 PM"

st.write(f"### Your Fooding Time: {fooding_time}")

# Display today's menu
today = datetime.datetime.today().strftime("%A")
today_menu = weekly_menu.get(today, "No menu available")
st.write(f"### Today's Menu: {today_menu}")

# Prices for items
prices = {
    "Sambar": 30,
    "Tomato Rice": 40,
    "Chicken": 70,
    "Brinjal": 25,
    "Lemon Rice": 35,
    "Curd Rice": 30,
}

# Quantity input for today's menu
quantity = st.number_input(f"Enter quantity for today's menu ({today_menu}):", min_value=1, max_value=10, value=1)

# Payment options
payment_method = st.radio(
    "Select Payment Method:",
    ("Pay at Counter", "Phone Pay")
)

# Phone number input only if Phone Pay selected
phone = ""
if payment_method == "Phone Pay":
    phone = st.text_input("Enter your phone number for Phone Pay:")

# Place Order button logic
if st.button("Place Order"):
    # Validations
    if not department.strip():
        st.error("⚠️ Please enter your department.")
    elif payment_method == "Phone Pay" and (not phone.isdigit() or len(phone) < 7):
        st.error("⚠️ Please enter a valid phone number for Phone Pay.")
    else:
        total_bill = prices.get(today_menu, 0) * quantity
        st.success("🎉 Order placed successfully!")
        st.markdown(f"**Department:** {department}")
        st.markdown(f"**Year:** {year}")
        st.markdown(f"**Fooding Time:** {fooding_time}")
        st.markdown(f"**Today's Item:** {today_menu} × {quantity}")
        st.markdown(f"**Total Bill:** Rs {total_bill}")
        st.markdown(f"**Payment Method:** {payment_method}")
        if payment_method == "Phone Pay":
            st.markdown(f"**Phone Number:** {phone}")
            st.info("Please complete the payment via Phone Pay and show the confirmation at pickup.")
        else:
            st.info("Please pay at the canteen counter when you pick up your order.")
