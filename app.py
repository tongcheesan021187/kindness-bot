import streamlit as st
from better_profanity import profanity

# 1. SETUP
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# 2. LOAD SAFETY FILTER
profanity.load_censor_words()

def is_safe(text):
    return not profanity.contains_profanity(text)

# 3. THE KNOWLEDGE BASE (The "Brain")
knowledge = {
    "what is": "Cyberkindness is treating others online with the same respect you'd show them in person! 💜",
    "cyberbullying": "Cyberbullying is repeated, mean behavior online. Remember: It's not your fault. Stop, Block, and Tell a trusted adult.",
    "stupid": "Being called names hurts. Don't reply—that's what they want. Take a screenshot and talk to a teacher or counselor.",
    "mean": "If someone is mean, use the 'Stop, Block, Tell' rule. Don't let their pixels ruin your day!",
    "report": "Most apps have a 'Report' button. In school, your CCE teacher or counselor is always here to help.",
    "anonymous": "Being anonymous isn't a license to be mean. Digital footprints are real and lasting!",
    "whatsapp": "Chat groups can get toxic. You have the right to mute or leave any group that makes you feel unsafe.",
    "help": "I can help with definitions of cyberbullying, tips on what to do if someone is mean, and how to be an 'Upstander'!"
}

# 4. THE INTERFACE
st.title("💜 The CyberKindness Booth")
st.markdown("Welcome to our VIA Project! Ask me about online safety.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to the CyberKindness Booth! 💜 Ask me something like 'What is cyberbullying?' to get started!"}
    ]

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. THE LOGIC
if prompt := st.chat_input("Type your question here..."):
    if not is_safe(prompt):
        st.error("🚫 **Safety Alert:** We only use kind language here. Please rephrase.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Bot Response
        user_input = prompt.lower()
        bot_reply = "That's an important topic. Remember, being an 'Upstander' means speaking up for others. Have you talked to a teacher about this?"

        for key, value in knowledge.items():
            if key in user_input:
                bot_reply = value
                break
        
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
