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

# --- 3. THE RE-ORDERED BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # PRIORITY 1: DEFINITIONS (Checking "What is" first)
    if "what is cyberbullying" in user_input or "define cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools (like WhatsApp, TikTok, or Discord) to "
            "repeatedly and intentionally hurt or harass someone. It includes spreading rumors, "
            "posting hurtful photos, or excluding others. Remember: If you wouldn't say it to "
            "their face, don't type it! 🚫"
        )
    
    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is choosing to be positive online! 🌈 It means being an "
            "Upstander, reporting meanness, and sending encouraging messages to make "
            "our school digital space safe for everyone."
        )

    # PRIORITY 2: HANDLING A BULLY / VICTIM ADVICE
    victim_triggers = ["handle", "deal", "bully", "victim", "mean", "what do i do", "happening to me", "bullied"]
    insults = ["ugly", "stupid", "idiot", "dumb", "noob", "loser", "weird", "fat"]
    
    if any(word in user_input for word in victim_triggers + insults):
        return (
            "If someone is being a bully, you have the power to stop the situation. "
            "Follow the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply or argue. Bullies want a reaction.\n"
            "🚫 **BLOCK:** Use the app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, like your teacher or parent.\n\n"
            "**Important:** Take a screenshot before you block them for evidence! 💜"
        )

    # PRIORITY 3: WHO TO CALL (Helplines)
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact", "talk to"]):
        return (
            "You don't have to deal with this alone. **Talk to these people:**\n\n"
            "- **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.\n"
            "- **TOUCHline (Counselling):** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180"
        )

    # PRIORITY 4: SUPPORTING FRIENDS
    if any(word in user_input for word in ["friend", "support", "upstander"]):
        return (
            "Being an **Upstander** is a superpower! 💜 Check-in privately with your friend, "
            "help them take screenshots, and offer to walk with them to see a teacher."
        )

    # DEFAULT RESPONSE
    return "That's an interesting point. At our booth, we believe in being 'Upstanders'. How do you think we can make our school chats Kinder?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! 💜 Ask me 'What is Cyberbullying?' or 'How do I handle a bully?'"}]

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
