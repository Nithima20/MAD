import streamlit as st
import datetime
import qrcode
from io import BytesIO

st.set_page_config(page_title="CKCET Canteen Pre-Order", page_icon="🏫🍽️")

st.title("CKCET Canteen Pre-Order App")

# Weekly menu
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
username = st.text_input("Enter your name:")

dept_option = {
    "1": "CSE",
    "2": "AIDS",
    "3": "EEE",
    "4": "ECE"
}
dept_choice = st.selectbox("Select your Department (Choose option):", options=list(dept_option.keys()), format_func=lambda x: f"{x}: {dept_option[x]}")

year = st.selectbox("Select your Year:", options=["1st Year", "2nd Year", "3rd Year", "Final Year"])

# Set fooding time based on year
if year in ["1st Year", "Final Year"]:
    fooding_time = "12:15 PM"
else:
    fooding_time = "1:00 PM"
st.write(f"### Your Fooding Time: {fooding_time}")

# Today’s menu and price list
today = datetime.datetime.today().strftime("%A")
today_menu = weekly_menu.get(today, "No menu available")

prices = {
    "Sambar": 30,
    "Tomato Rice": 40,
    "Chicken": 70,
    "Brinjal": 25,
    "Lemon Rice": 35,
    "Curd Rice": 30,
}

st.write(f"### Today's Menu: {today_menu} (Rs {prices.get(today_menu,0)})")

quantity = st.number_input(f"Enter quantity for today's menu ({today_menu}):", min_value=1, max_value=10, value=1)

# Payment options
payment_method = st.radio("Select Payment Method:", ["Pay at Counter", "Phone Pay"])

phone = ""
if payment_method == "Phone Pay":
    phone = st.text_input("Enter your phone number for Phone Pay:")

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buf = BytesIO()
    img.save(buf)
    return buf

if st.button("Place Order"):
    if not username.strip():
        st.error("⚠️ Please enter your name.")
    elif not dept_choice:
        st.error("⚠️ Please select your department.")
    elif payment_method == "Phone Pay" and (not phone.isdigit() or len(phone) < 7):
        st.error("⚠️ Please enter a valid phone number for Phone Pay.")
    else:
        total_bill = prices.get(today_menu, 0) * quantity
        st.success("🎉 Order placed successfully!")
        st.markdown(f"**Name:** {username}")
        st.markdown(f"**Department:** {dept_option[dept_choice]} ({dept_choice})")
        st.markdown(f"**Year:** {year}")
        st.markdown(f"**Fooding Time:** {fooding_time}")
        st.markdown(f"**Item:** {today_menu} × {quantity}")
        st.markdown(f"**Total Bill:** Rs {total_bill}")
        st.markdown(f"**Payment Method:** {payment_method}")

        if payment_method == "Phone Pay":
            st.markdown(f"**Phone Number:** {phone}")
            st.info("Scan this QR code to pay the total amount:")

            # Generate QR code data string - replace this with your actual payment link or UPI string
            upi_string = f"upi://pay?pa=your-merchant-vpa@bank&pn=CKCET+Canteen&am={total_bill}&cu=INR&tn=Food+Payment"
            
            qr_img_buf = generate_qr_code(upi_string)
            st.image(qr_img_buf, width=250)
            st.write("After payment, please show the confirmation at pickup.")
        else:
            st.info("Please pay at the canteen counter when you pick up your order.")
