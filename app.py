import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
# Instead of an external library, we use our own list for total control.
def check_safety(text):
    # 1. These are words that ARE allowed (students can ask about them)
    allowed_words = ["stupid", "ugly", "idiot", "dumb", "noob", "loser", "shut up"]
    
    # 2. These are the ONLY words that will trigger the "Safety Alert"
    # Add any specific severe vulgarities here that you want to block.
    blocked_words = ["insert_extreme_vulgarity_1", "insert_extreme_vulgarity_2"] 
    
    user_words = text.lower().split()
    for word in user_words:
        # Clean the word of punctuation (like "stupid!")
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word in blocked_words:
            return False
    return True

# --- 3. THE KNOWLEDGE BASE ---
knowledge = {
    "what is": "Cyberkindness is treating others online with the same respect you'd show them in person! 💜",
    "cyberbullying": "Cyberbullying is repeated, mean behavior online. It's not your fault. Stop, Block, and Tell a trusted adult.",
    "stupid": "Being called names like 'stupid' hurts. Don't reply—that's what the bully wants. Take a screenshot and talk to a teacher.",
    "ugly": "If someone calls you names like 'ugly', remember their behavior says more about them than you. Block them and move on!",
    "mean": "If someone is mean, use the 'Stop, Block, Tell' rule. Don't let their pixels ruin your day!",
    "report": "Most apps have a 'Report' button. In school, your CCE teacher or counselor is always here to help.",
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
        bot_response = "That's an important point. In our school, we believe in being 'Upstanders'. Have you shared this with a teacher?"

        for key, value in knowledge.items():
            if key in user_text:
                bot_response = value
                break
        
        with st.chat_message("assistant"):
            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
