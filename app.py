import streamlit as st
from better_profanity import profanity

# --- CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Helper", page_icon="🤝")

# Pre-load profanity filter
profanity.load_censor_words()

def is_safe(text):
    return not profanity.contains_profanity(text)

# --- THE BOT'S KNOWLEDGE BASE ---
# This is where you can add more questions and answers!
responses = {
    "cyberbullying": "Cyberbullying is using digital tools (like social media or WhatsApp) to deliberate hurt, upset, or harass someone. It's never okay.",
    "stupid": "I'm sorry to hear that. Being called names hurts. Remember: their words don't define you. You should take a screenshot and talk to a trusted adult or teacher.",
    "mean": "If someone is being mean online, the best first step is 'Stop, Block, and Tell'. Don't reply to the meanness, block the user, and tell someone you trust.",
    "report": "In Singapore, most apps like Instagram and TikTok have 'Report' buttons. You can also talk to your school counselor or a teacher if it's happening in school chats.",
    "kindness": "Cyberkindness is about being an 'Upstander'—someone who stands up for others and spreads positivity instead of hate!",
    "sticker": "That's a great idea! Maybe you can design a 'Kindness Sticker' for your VIA project to remind people to think before they post.",
}

# --- UI ---
st.title("🤝 CyberKindness Advocate")
st.info("I am here to help you deal with online meanness and plan your VIA project. Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Type a question like 'What is cyberbullying?' or tell me about something that happened online."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type here..."):
    if not is_safe(prompt):
        st.error("⚠️ Please use kind language. I cannot respond to vulgarities.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # LOGIC: Search for keywords in the user's message
        user_text = prompt.lower()
        bot_answer = "That's an interesting point. How do you think we can promote more kindness in our school regarding that?" # Default

        for keyword, reply in responses.items():
            if keyword in user_text:
                bot_answer = reply
                break 

        with st.chat_message("assistant"):
            st.markdown(bot_answer)
            st.session_state.messages.append({"role": "assistant", "content": bot_answer})
