import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    # Only heavy vulgarities go here.
    blocked_words = ["insert_extreme_vulgarity_1", "insert_extreme_vulgarity_2"] 
    user_words = text.lower().split()
    for word in user_words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word in blocked_words:
            return False
    return True

# --- 3. THE "NO-FAIL" BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # 1. THE EMERGENCY TRIGGER (Stop, Block, Tell)
    # This covers "bullies me", "victim", "help", "handle", and all insults.
    emergency_keywords = ["bully", "bullied", "mean", "victim", "handle", "deal", "what do i do", "ugly", "stupid", "idiot", "dumb", "noob"]
    if any(word in user_input for word in emergency_keywords):
        return (
            "If someone is being mean to you, remember the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply. Don't give them the reaction they want.\n"
            "🚫 **BLOCK:** Use the app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, teacher, or counselor.\n\n"
            "**Don't forget:** Take a screenshot for evidence before you block! 💜"
        )

    # 2. DEFINITIONS
    if "cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools (WhatsApp, TikTok, etc.) to "
            "repeatedly and intentionally hurt or harass someone. "
            "If you wouldn't say it to their face, don't type it! 🚫"
        )
    
    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is choosing to be an Upstander, reporting meanness, "
            "and sending encouraging messages to keep our school community safe. 🌈"
        )

    # 3. HELPLINES
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact"]):
        return (
            "You are not alone. **Talk to:**\n"
            "- **In School:** Your Form Teacher or School Counselor.\n"
            "- **TOUCHline:** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180"
        )

    # 4. SUPPORTING FRIENDS
    if any(word in user_input for word in ["friend", "support", "upstander"]):
        return (
            "Be an **Upstander**! 💜 Check-in privately, help them take screenshots, "
            "and offer to walk with them to tell a teacher."
        )

    # DEFAULT
    return "That's an important point for our booth! How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! 💜 Ask me 'How do I handle a bully?' or 'What is cyberbullying?'"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Ask about help, friends, or kindness..."):
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
