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

# --- 3. THE "CATCH-ALL" BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # 1. DEFINITION CHECK (Must be first to avoid confusion)
    if "what is cyberbullying" in user_input or "define cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools (like WhatsApp, TikTok, or Discord) to "
            "repeatedly and intentionally hurt or harass someone. It includes spreading rumors, "
            "posting hurtful photos, or excluding others. Remember: If you wouldn't say it to "
            "their face, don't type it! 🚫"
        )

    # 2. EMERGENCY ADVICE (Stop, Block, Tell)
    # Added "online", "chat", "someone", and "internet" triggers
    emergency_triggers = [
        "bully", "bullied", "bullies", "mean", "victim", "handle", "deal", 
        "what do i do", "online", "internet", "someone", "ugly", "stupid"
    ]
    
    if any(word in user_input for word in emergency_triggers):
        return (
            "If someone is being mean to you online, remember the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply. Don't give them the reaction they want.\n"
            "🚫 **BLOCK:** Use the app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, like a parent, teacher, or counselor.\n\n"
            "**Don't forget:** Take a screenshot for evidence before you block! 💜"
        )

    # 3. HELPLINES
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact"]):
        return (
            "You don't have to deal with this alone. **Talk to:**\n"
            "- **In School:** Your Form Teacher or School Counselor.\n"
            "- **TOUCHline:** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180"
        )

    # 4. SUPPORTING FRIENDS
    if any(word in user_input for word in ["friend", "support", "upstander"]):
        return (
            "Be an **Upstander**! 💜 Check-in privately with your friend, "
            "help them take screenshots, and offer to walk with them to see a teacher."
        )

    # 5. CYBERKINDNESS
    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is choosing to be an Upstander and sending "
            "encouraging messages to make our digital space safe for everyone. 🌈"
        )

    # DEFAULT
    return "That's an important point for our booth! We are advocating for a safer school internet. How do you think we can help our classmates stay kind in our school chats?"

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
