import streamlit as st
import uuid
from datetime import datetime

# Menu
menu = {
    1: {"name": "Burger", "price": 50},
    2: {"name": "Pizza", "price": 100},
    3: {"name": "Sandwich", "price": 40},
    4: {"name": "Pasta", "price": 80},
    5: {"name": "Juice", "price": 30},
}

# App Title
st.title("Canteen Pre-Order App")

# Menu Display
st.write("### Today's Menu:")
for key, item in menu.items():
    st.write(f"{key}. {item['name']} - Rs {item['price']}")

# User Details
user_name = st.text_input("Enter your name:")

# How many items
total_items = st.number_input(
    "How many different items do you want to order?",
    min_value=1,
    max_value=len(menu),
    value=1
)

# Order Input
order = {}
selected_items = set()

for i in range(total_items):
    col1, col2 = st.columns(2)
    with col1:
        available_options = [k for k in menu if k not in selected_items]
        item_number = st.selectbox(
            f"Select item #{i + 1}",
            options=available_options,
            key=f"item_{i}"
        )
        selected_items.add(item_number)
    with col2:
        quantity = st.number_input(
            f"Quantity for item #{i + 1}",
            min_value=1,
            max_value=20,
            value=1,
            key=f"qty_{i}"
        )
    order[item_number] = quantity

# Pickup time input with basic validation
pickup_time = st.text_input("Enter preferred pickup time (e.g., 12:30 PM):", value="12:00 PM")

def is_valid_time(time_str):
    try:
        datetime.strptime(time_str, "%I:%M %p")  # e.g., 12:30 PM
        return True
    except ValueError:
        return False

# Place Order Button
if st.button("Place Order"):
    if not user_name.strip():
        st.error("Please enter your name.")
    elif not is_valid_time(pickup_time):
        st.error("Please enter pickup time in format like '12:30 PM'.")
    else:
        total_cost = sum(menu[item]['price'] * qty for item, qty in order.items())
        order_id = str(uuid.uuid4())[:8]  # Short unique ID

        # Order Summary
        st.write("### Order Confirmation")
        st.write(f"**Order ID:** {order_id}")
        st.write(f"**Customer Name:** {user_name}")
        st.write(f"**Pickup Time:** {pickup_time}")
        st.write("**Order Summary:**")
        for item, qty in order.items():
            st.write(f"{menu[item]['name']} x {qty} = Rs {menu[item]['price'] * qty}")
        st.write(f"**Total Cost:** Rs {total_cost}")
        st.success("Thank you for using the Canteen Pre-Order App!")

