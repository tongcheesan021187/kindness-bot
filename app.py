import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    # Severe vulgarities go here.
    blocked_words = ["insert_extreme_vulgarity_1", "insert_extreme_vulgarity_2"] 
    user_words = text.lower().split()
    for word in user_words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word in blocked_words:
            return False
    return True

# --- 3. THE RE-ORDERED BRAIN (Priority System) ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # --- PRIORITY 1: ACTS AND EXAMPLES (Checked First) ---
    if any(word in user_input for word in ["acts", "examples", "types", "looks like"]):
        # If they ask for KINDNESS acts specifically
        if "kindness" in user_input:
            return (
                "**Acts of Cyberkindness** make the internet better! 🌈\n\n"
                "1. **Checking In:** Private messaging someone who was bullied to see if they are okay.\n"
                "2. **Reporting:** Flagging mean content instead of sharing or 'liking' it.\n"
                "3. **Including:** Inviting someone who is being left out into a group chat.\n"
                "4. **Positive Comments:** Leaving encouraging words on a classmate's post.\n"
                "5. **Evidence Help:** Helping a friend take screenshots of meanness to report it."
            )
        # Otherwise, show BULLYING acts
        return (
            "Cyberbullying can look like many things. Common **acts** include:\n\n"
            "1. **Harassment:** Sending mean, threatening, or hurtful messages repeatedly.\n"
            "2. **Exclusion:** Intentionally leaving someone out of a group chat to be mean.\n"
            "3. **Outing:** Sharing someone's private secrets or photos without their permission.\n"
            "4. **Impersonation:** Creating a fake account to make someone look bad.\n"
            "5. **Flaming:** Using nasty language to start an online fight.\n\n"
            "If you see these, remember to be an Upstander! ✋"
        )

    # --- PRIORITY 2: DEFINITIONS ---
    if "what is cyberbullying" in user_input or "define cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools (like WhatsApp, TikTok, or Discord) to "
            "repeatedly and intentionally hurt or harass someone. \n\n"
            "**The Golden Rule:** If you wouldn't say it to their face, don't type it! 🚫"
        )
    
    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is choosing to be an Upstander, reporting meanness, "
            "and sending encouraging messages to keep our school community safe. 🌈"
        )

    # --- PRIORITY 3: EMERGENCY ADVICE (Stop, Block, Tell) ---
    # Only triggers if the user didn't ask for a definition or acts above.
    emergency_keywords = ["handle", "deal", "victim", "help me", "ugly", "stupid", "idiot", "loser", "bully", "bullied"]
    if any(word in user_input for word in emergency_keywords) or user_input.startswith("how"):
        return (
            "If someone is being mean to you online, follow the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply. Don't give them the reaction they want.\n"
            "🚫 **BLOCK:** Use app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, teacher, or counselor.\n\n"
            "**Pro-tip:** Take a screenshot for evidence first! 💜"
        )

    # --- PRIORITY 4: HELPLINES ---
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact"]):
        return (
            "You don't have to deal with this alone. **Talk to:**\n"
            "- **In School:** Your Form Teacher or School Counselor.\n"
            "- **TOUCHline:** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180 📞"
        )

    # DEFAULT
    return "That's an important point for our booth! How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! 💜 Ask me 'What are some acts of cyberbullying?' or 'How do I handle a bully?'"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Ask about kindness, help, or acts..."):
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
