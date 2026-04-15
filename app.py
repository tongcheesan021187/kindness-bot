import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    blocked_words = ["insert_extreme_vulgarity_1", "insert_extreme_vulgarity_2"] 
    user_words = text.lower().split()
    for word in user_words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word in blocked_words:
            return False
    return True

# --- 3. THE "ALL-ACCESS" BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # TOPIC 1: EXAMPLES/ACTS OF CYBERBULLYING
    if any(word in user_input for word in ["acts", "examples", "types", "looks like"]):
        return (
            "Cyberbullying can take many forms. Some common **acts** include:\n\n"
            "1. **Harassment:** Sending mean or threatening messages repeatedly.\n"
            "2. **Exclusion:** Intentionally leaving someone out of group chats or online games.\n"
            "3. **Outing:** Sharing someone's private secrets or embarrassing photos without permission.\n"
            "4. **Flaming:** Starting online fights using nasty and offensive language.\n"
            "5. **Impersonation:** Creating fake profiles to make someone look bad.\n\n"
            "If you see these happening, it's time to be an Upstander! ✋"
        )

    # TOPIC 2: DEFINITIONS
    if "what is cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools (WhatsApp, TikTok, Discord, etc.) to "
            "repeatedly and intentionally hurt or harass someone. "
            "Remember: If you wouldn't say it to their face, don't type it! 🚫"
        )

    # TOPIC 3: EMERGENCY ADVICE (Stop, Block, Tell)
    # This triggers if they ask "how", "handle", "victim", or use insults
    emergency_keywords = ["handle", "deal", "victim", "help me", "ugly", "stupid", "idiot", "loser"]
    if any(word in user_input for word in emergency_keywords) or user_input.startswith("how"):
        return (
            "If someone is being mean to you online, use the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply. Don't give them the reaction they want.\n"
            "🚫 **BLOCK:** Use the app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, teacher, or counselor.\n\n"
            "**Pro-tip:** Take a screenshot for evidence before you block! 💜"
        )

    # TOPIC 4: CONTACTS & HELPLINES
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact"]):
        return (
            "You don't have to deal with this alone. **Talk to:**\n"
            "- **In School:** Your Form Teacher or School Counselor.\n"
            "- **TOUCHline:** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180 📞"
        )

    # TOPIC 5: CYBERKINDNESS
    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is choosing to be an Upstander, reporting meanness, "
            "and sending encouraging messages to keep our school community safe. 🌈"
        )

    # DEFAULT
    return "That's an important point for our booth! How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! 💜 Ask me 'What are some acts of cyberbullying?' or 'Who can I call for help?'"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Ask about help, acts, or kindness..."):
    if not check_safety(prompt):
        st.error("🚫 **Safety Alert:** Please use respectful language.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        bot_response = get_bot_response(prompt)
        with st.chat_message("assistant"):
            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
