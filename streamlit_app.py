import streamlit as st
import uuid
from datetime import datetime

# Set page config
st.set_page_config(page_title="Canteen Pre-Order", page_icon="🍽️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #fefae0;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #283618;
    }
    .stButton > button {
        background-color: #bc6c25;
        color: white;
        border: None;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton > button:hover {
        background-color: #dda15e;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.title("🍽️ Canteen Pre-Order App")

    # Menu
    menu = {
        1: {"name": "Burger", "price": 50},
        2: {"name": "Pizza", "price": 100},
        3: {"name": "Sandwich", "price": 40},
        4: {"name": "Pasta", "price": 80},
        5: {"name": "Juice", "price": 30},
    }

    st.markdown("### 🧾 Today's Menu:")
    for key, item in menu.items():
        st.markdown(f"`{key}.` **{item['name']}** – ₹{item['price']}")

    st.markdown("---")

    # User Details
    user_name = st.text_input("👤 Enter your name:")

    # Number of items
    total_items = st.number_input(
        "🛒 How many different items do you want to order?",
        min_value=1, max_value=len(menu), value=1
    )

    # Item selection
    order = {}
    selected_items = set()

    for i in range(total_items):
        st.markdown(f"**🍴 Item #{i+1}**")
        col1, col2 = st.columns(2)
        with col1:
            available_options = [k for k in menu if k not in selected_items]
            item_number = st.selectbox(
                "Select item:",
                options=available_options,
                format_func=lambda x: menu[x]['name'],
                key=f"item_{i}"
            )
            selected_items.add(item_number)
        with col2:
            quantity = st.number_input(
                "Quantity:",
                min_value=1, max_value=20, value=1, key=f"qty_{i}"
            )
        order[item_number] = quantity

    # Pickup Time
    pickup_time = st.text_input("⏰ Enter preferred pickup time (e.g., 12:30 PM):", value="12:00 PM")

    def is_valid_time(time_str):
        try:
            datetime.strptime(time_str, "%I:%M %p")
            return True
        except ValueError:
            return False

    # Order Button
    if st.button("✅ Place Order"):
        if not user_name.strip():
            st.error("Please enter your name.")
        elif not is_valid_time(pickup_time):
            st.error("Please enter a valid time (e.g., 01:15 PM)")
        else:
            total_cost = sum(menu[item]['price'] * qty for item, qty in order.items())
            order_id = str(uuid.uuid4())[:8]

            st.success("🎉 Order Placed Successfully!")
            st.markdown("### 🧾 Order Summary:")
            st.markdown(f"**🆔 Order ID:** `{order_id}`")
            st.markdown(f"**👤 Name:** {user_name}")
            st.markdown(f"**⏰ Pickup Time:** {pickup_time}")
            for item, qty in order.items():
                st.markdown(f"- {menu[item]['name']} × {qty} = ₹{menu[item]['price'] * qty}")
            st.markdown(f"**💰 Total Cost:** ₹{total_cost}")
