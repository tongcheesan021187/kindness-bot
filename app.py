import streamlit as st
from better_profanity import profanity

# --- SETUP ---
st.set_page_config(page_title="CyberKindness Bot", page_icon="💜")

# Standard profanity check
profanity.load_censor_words()

def is_safe(text):
    return not profanity.contains_profanity(text)

# --- THE KNOWLEDGE BASE ---
# We use keywords to trigger specific advice for your classmates
knowledge = {
    "hello": "Hi there! I'm the CyberKindness Bot. I'm here to help you navigate the digital world safely. How are you feeling today?",
    "what is cyberkindness": "Cyberkindness is about treating others online the same way you'd treat them face-to-face—with respect, empathy, and heart! 💜",
    "cyberbullying": "Cyberbullying is when someone uses the internet to meanly target others. If it's happening to you, remember: It is NOT your fault. Stop, Block, and Tell a trusted adult.",
    "stupid": "Words like that can really sting. If someone calls you names online, don't retaliate. That's what they want. Instead, take a screenshot for evidence and block them.",
    "ugly": "Ouch. Remember that people often say mean things online because they are unhappy themselves. Don't let their pixels ruin your day!",
    "sticker": "If you're at our booth, grab a physical sticker! They are a reminder to 'Think Before You Post'.",
    "report": "On most apps, you can report a comment or profile. In school, you can always talk to your Character & Citizenship Education (CCE) teacher or a counselor.",
    "anonymous": "People think being anonymous means they can be mean, but digital footprints are real. True strength is being kind even when no one knows it's you.",
    "whatsapp": "Chat groups can get toxic fast. If a group chat is turning mean, you can leave the group or mute it. You don't owe anyone your mental peace!",
    "help": "I can help with: \n1. Defining cyberbullying \n2. What to do if someone is mean \n3. How to be a better friend online. What's on your mind?"
}

# --- USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("""
Welcome to our VIA Project! This chatbot is designed to help us make our school's digital space safer. 
**Type a question or tell me about a situation you've seen online.**
""")

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! I'm here to listen. You can ask me 'What is cyberbullying?' or tell me about a problem you're facing."}]

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Message the CyberKindness Bot..."):
    
    if not is_safe(prompt):
        st.error("🚫 **Safety Alert:** We promote kindness here. Please rephrase your message without using vulgarities.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Logic to find the best response
        user_input = prompt.lower()
        found_reply = "I'm still learning! But remember: when in doubt, the best move online is to be kind or stay silent. Have you spoken to a teacher about this?"

        for key, value in knowledge.items():
            if key in user_input:
                found_reply = value
                break
        
        with st.chat_message("assistant"):
            st.markdown(found_reply)
            st.session_state.messages.append({"role": "assistant", "content": found_reply})
