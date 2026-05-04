import streamlit as st
from datetime import datetime
import uuid

# -------------------- CLASSES --------------------
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def clear_cart(self):
        self.items = []

class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cart = Cart()

class Order:
    def __init__(self, user, items):
        self.order_id = str(uuid.uuid4())[:8]
        self.user = user
        self.items = items
        self.total = sum(item.price for item in items)
        self.time = datetime.now()

# -------------------- INIT SESSION --------------------
if "system" not in st.session_state:
    system = {
        "restaurants": [],
        "orders": []
    }

    # Create restaurants
    r1 = Restaurant("Pizza Hub")
    r1.add_item(MenuItem("Pizza", 250))
    r1.add_item(MenuItem("Cheese Pizza", 300))

    r2 = Restaurant("Burger Point")
    r2.add_item(MenuItem("Burger", 120))
    r2.add_item(MenuItem("Paneer Burger", 180))

    system["restaurants"] = [r1, r2]
    st.session_state.system = system

if "user" not in st.session_state:
    st.session_state.user = User("Nitin", "Bhopal")

# -------------------- UI --------------------
st.title("🍔 Food Delivery App")

system = st.session_state.system
user = st.session_state.user

# -------------------- SHOW RESTAURANTS --------------------
st.header("Restaurants")

for i, r in enumerate(system["restaurants"]):
    st.subheader(f"{r.name}")

    for item in r.menu:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{item.name} - ₹{item.price}")
        with col2:
            if st.button(f"Add {item.name}", key=f"{r.name}-{item.name}"):
                user.cart.add_to_cart(item)
                st.success(f"{item.name} added!")

# -------------------- CART --------------------
st.header("🛒 Cart")

if user.cart.items:
    total = 0
    for item in user.cart.items:
        st.write(f"{item.name} - ₹{item.price}")
        total += item.price

    st.write(f"### Total: ₹{total}")

    # Place Order
    if st.button("Place Order"):
        order = Order(user, user.cart.items)
        system["orders"].append(order)
        user.cart.clear_cart()

        st.success("✅ Order Placed Successfully!")

        st.subheader("Order Details")
        st.write(f"Order ID: {order.order_id}")
        st.write(f"User: {order.user.name}")
        st.write("Items:")
        for item in order.items:
            st.write(f"- {item.name}")
        st.write(f"Total: ₹{order.total}")
        st.write(f"Time: {order.time}")

else:
    st.info("Cart is empty")