import streamlit as st
from better_profanity import profanity

# --- CONFIGURATION & SAFEGUARDS ---
st.set_page_config(page_title="CyberKindness Advocate", page_icon="🛡️")

# Custom list of words to block (can be expanded)
custom_bad_words = ["badword1", "badword2"] 
profanity.add_censor_words(custom_bad_words)

def is_safe(text):
    """Checks if the input contains vulgarities."""
    return not profanity.contains_profanity(text)

# --- CHATBOT UI ---
st.title("🛡️ VIA: CyberKindness Advocate")
st.markdown("""
Welcome! Use this bot to plan your **CyberKindness** advocacy project. 
Type your ideas below to get started. 
*Note: This bot has a strict no-vulgarity policy.*
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm here to help you plan your VIA project. What's the main goal of your cyberkindness campaign?"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CHAT LOGIC ---
if prompt := st.chat_input("Share your project idea..."):
    
    # Check for vulgarity
    if not is_safe(prompt):
        st.error("⚠️ Message blocked: Please use kind and appropriate language.")
    else:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response (Simple Logic for VIA planning)
        with st.chat_message("assistant"):
            response = ""
            lower_prompt = prompt.lower()

            if "instagram" in lower_prompt or "social media" in lower_prompt:
                response = "Social media is a powerful tool! How will you ensure your posts reach your schoolmates? Maybe a specific hashtag or a poster with a QR code?"
            elif "workshop" in lower_prompt or "talk" in lower_prompt:
                response = "An interactive session is great. What's one 'Golden Rule' of the internet you want to teach them?"
            elif "cyberbullying" in lower_prompt:
                response = "Addressing bullying is crucial. Your project could focus on how to be an 'Upstander' instead of a 'Bystander'."
            else:
                response = "That sounds like a solid start! How can we make this project more engaging for other Secondary 1-5 students?"

            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
