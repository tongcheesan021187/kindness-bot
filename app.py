import streamlit as st
from better_profanity import profanity

# 1. PAGE SETUP
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# 2. CONFIGURE SAFETY FILTER
# We load the standard list but "whitelist" school-level insults 
# so the bot can actually discuss them and give advice.
profanity.load_censor_words()
words_to_allow = ["stupid", "ugly", "idiot", "dumb", "noob", "loser"]
profanity.remove_censor_words(words_to_allow)

def is_safe(text):
    # Returns True if the text is clean of heavy vulgarities
    return not profanity.contains_profanity(text)

# 3. KNOWLEDGE BASE (Keywords and Responses)
knowledge = {
    "what is": "Cyberkindness is treating others online with the same respect you'd show them in person! 💜",
    "cyberbullying": "Cyberbullying is repeated, mean behavior online. Remember: It's not your fault. Stop, Block, and Tell a trusted adult.",
    "stupid": "Being called names like 'stupid' hurts. Don't reply—that's what the bully wants. Take a screenshot and talk to a teacher or counselor.",
    "ugly": "If someone calls you names like 'ugly', remember that their behavior says more about them than it does about you. Block them and move on!",
    "mean": "If someone is mean, use the 'Stop, Block, Tell' rule. Don't let their pixels ruin your day!",
    "report": "Most apps have a 'Report' button. In school, your CCE teacher or counselor is always here to help.",
    "anonymous": "Being anonymous isn't a license to be mean. Digital footprints are real and lasting!",
    "whatsapp": "Chat groups can get toxic. You have the right to mute or leave any group that makes you feel unsafe.",
    "help": "I can help with: \n1. Dealing with insults \n2. Reporting bullying \n3. How to be an 'Upstander'."
}

# 4. THE INTERFACE
st.title("💜 The CyberKindness Booth")
st.markdown("Welcome to our VIA Project! Ask me about online safety or share a situation you've seen.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to the CyberKindness Booth! 💜 How can I help you stay safe online today?"}
    ]

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. THE CHAT LOGIC
if prompt := st.chat_input("Type your question here..."):
    # First, check for actual vulgarity
    if not is_safe(prompt):
        st.error("🚫 **Safety Alert:** Please do not use vulgar language. We are here to promote kindness!")
    else:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Look for keywords in the user's input
        user_input = prompt.lower()
        bot_reply = "That's an important point. In our school, we believe in being 'Upstanders' who support one another. Have you shared this with a teacher?"

        for key, value in knowledge.items():
            if key in user_input:
                bot_reply = value
                break
        
        # Show bot response
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
