import streamlit as st

menu = {
    1: {"name": "Burger", "price": 50},
    2: {"name": "Pizza", "price": 100},
    3: {"name": "Sandwich", "price": 40},
    4: {"name": "Pasta", "price": 80},
    5: {"name": "Juice", "price": 30},
}

st.title("Canteen Pre-Order App")

st.write("### Today's Menu:")
for key, item in menu.items():
    st.write(f"{key}. {item['name']} - Rs {item['price']}")

# How many items
total_items = st.number_input("How many different items do you want to order?", min_value=1, max_value=10, value=1)

order = {}

for i in range(total_items):
    col1, col2 = st.columns(2)
    with col1:
        item_number = st.selectbox(f"Select item #{i+1}", options=list(menu.keys()), key=f"item_{i}")
    with col2:
        quantity = st.number_input(f"Quantity for item #{i+1}", min_value=1, max_value=20, value=1, key=f"qty_{i}")
    order[item_number] = order.get(item_number, 0) + quantity

pickup_time = st.text_input("Enter preferred pickup time (e.g., 12:30 PM):", value="12:00 PM")

if st.button("Place Order"):
    total_cost = sum(menu[item]['price'] * qty for item, qty in order.items())
    st.write("### Your Order Summary:")
    for item, qty in order.items():
        st.write(f"{menu[item]['name']} x {qty} = Rs {menu[item]['price'] * qty}")
    st.write(f"**Pickup Time:** {pickup_time}")
    st.write(f"**Total Cost:** Rs {total_cost}")
    st.success("Thank you for using the Canteen Pre-Order App!")
