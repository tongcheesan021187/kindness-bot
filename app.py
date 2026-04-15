import streamlit as st
from better_profanity import profanity

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. SAFETY FILTER SETUP ---
if 'filter_ready' not in st.session_state:
    profanity.load_censor_words()
    # List of words we want the bot to ALLOW so it can talk about them
    allowed = {"stupid", "ugly", "idiot", "dumb", "noob", "loser", "shut up"}
    custom_bad_words = [w for w in profanity.CENSOR_WORDSET if w not in allowed]
    profanity.load_censor_words(custom_bad_words)
    st.session_state['filter_ready'] = True

def check_safety(text):
    return not profanity.contains_profanity(text)

# --- 3. THE KNOWLEDGE BASE ---
knowledge = {
    "what is": "Cyberkindness is treating others online with the same respect you'd show them in person! 💜",
    "cyberbullying": "Cyberbullying is repeated, mean behavior online. Remember: It's not your fault. Stop, Block, and Tell a trusted adult.",
    "stupid": "Being called names like 'stupid' hurts. Don't reply—that's what the bully wants. Take a screenshot and talk to a teacher or counselor.",
    "ugly": "If someone calls you names like 'ugly', remember that their behavior says more about them than it does about you. Block them and move on!",
    "mean": "If someone is mean, use the 'Stop, Block, Tell' rule. Don't let their pixels ruin your day!",
    "report": "Most apps (IG, TikTok, WhatsApp) have a 'Report' button. In school, your CCE teacher or counselor is always here to help.",
    "anonymous": "Being anonymous isn't a license to be mean. Digital footprints are real and lasting!",
    "whatsapp": "Chat groups can get toxic. You have the right to mute or leave any group that makes you feel unsafe.",
    "help": "I can help with: 1. Dealing with insults, 2. Reporting bullying, or 3. How to be an 'Upstander'."
}

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("Welcome to our VIA Project! Ask a question or share a situation you've seen online.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to the CyberKindness Booth! 💜 How can I help you stay safe online today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Type here..."):
    if not check_safety(prompt):
        st.error("🚫 **Safety Alert:** We only use kind language here. Please rephrase your message.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        user_text = prompt.lower()
        bot_response = "That's an important point. In our school, we believe in being 'Upstanders' who support one another. Have you shared this with a teacher?"

        for key, value in knowledge.items():
            if key in user_text:
                bot_response = value
                break
        
        with st.chat_message("assistant"):
            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
