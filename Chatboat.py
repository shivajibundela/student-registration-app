import streamlit as st

st.title("🤖 AI Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.write(msg)

# User input
user = st.text_input("Human:")

if user:
    response = ""

    if user.lower() in ["hii", "hey", "hello", "oii", "he"]:
        response = "Bot: Hii Human! How may I help you?"

    elif "python" in user.lower():
        response = "Bot: Python is a high-level, interpreted programming language that is easy to read and write.\nBot: Are you happy with response?"

    elif user.lower() in ["yes", "no"]:
        response = "Bot: Thank you for your valuable feedback"

    elif "data science" in user.lower():
        response = "Bot: Data Science involves collecting, analyzing, and interpreting data.\nBot: Are you happy with response?"

    elif user.lower() in ["exit", "end", "bye", "close"]:
        response = "Bot: Bye bye, have a nice day"

    else:
        response = "Bot: This is not in our domain. Try another prompt."

    # Save chat
    st.session_state.messages.append(f"Human: {user}")
    st.session_state.messages.append(response)

    # Show response
    st.write(response)