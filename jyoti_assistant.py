
import streamlit as st

st.set_page_config(
    page_title="Jyoti Assistant",
    page_icon="🌸"
)

st.title("🌸 Welcome to Jyoti AI Shopping Assistant")
st.write("Your favourite destination for fashion and beauty! 🌸")

st.write(
    "Ask me about dresses, sarees, skincare, "
    "makeup and fashion."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to Jyoti Cloud Mart. How can I help you today?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("What would you like to know?")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    q = question.lower()

    if "dress" in q:
        answer = "We have maxi dresses, midi dresses and party dresses. 🌸"

    elif "saree" in q:
        answer = "Explore our ethnic wear collection for beautiful sarees!"

    elif "skincare" in q or "skin" in q:
        answer = "We offer serums, face oils and moisturisers."

    elif "makeup" in q:
        answer = "Explore our makeup collection, including lipsticks and brushes."

    elif "hello" in q or "hi" in q:
        answer = "Hello! 😊 How can I help you shop today?"

    else:
        answer = "I'd love to help! Please ask me about dresses, sarees, skincare or makeup."

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()
