import streamlit as st 

st.set_page_config(page_title="Student App", layout="wide") 

st.title("🎓 Student Registration System") 

# Sidebar 
st.sidebar.header("Input Details") 

name = st.sidebar.text_input("Name") 
age = st.sidebar.slider("Age", 10, 50) 
course = st.sidebar.selectbox("Course", ["BTech", "MBA", "MBBS"]) 

# Main layout 
col1, col2 = st.columns(2) 

with col1: 
   st.subheader("📌 Input Summary") 
   st.write("Name:", name) 
   st.write("Age:", age) 
   st.write("Course:", course) 

with col2: 
   st.subheader("📊 Analysis") 
   if age > 25: 
       st.warning("Late admission age") 
   else: 
       st.success("Good to go!") 