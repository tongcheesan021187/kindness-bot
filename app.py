import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    # Add severe vulgarities here to block them.
    blocked_words = ["insert_extreme_vulgarity_1", "insert_extreme_vulgarity_2"] 
    user_words = text.lower().split()
    for word in user_words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word in blocked_words:
            return False
    return True

# --- 3. THE "PERMANENT" BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # --- LEVEL 1: SPECIFIC DEFINITIONS (Checked First) ---
    # We use very specific phrase matching so these aren't "stolen" by other categories.
    if "what is cyberbullying" in user_input or "define cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools (WhatsApp, TikTok, etc.) to repeatedly "
            "and intentionally hurt or harass someone. It includes spreading rumors, posting "
            "hurtful photos, or excluding others. Remember: If you wouldn't say it to their "
            "face, don't type it! 🚫"
        )
    
    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is choosing to be an Upstander, reporting meanness, "
            "and sending encouraging messages to keep our school community safe. 🌈"
        )

    # --- LEVEL 2: EMERGENCY ACTION (Stop, Block, Tell) ---
    # This triggers for names/insults OR direct questions about handling a bully.
    insults = ["ugly", "stupid", "idiot", "dumb", "noob", "loser", "weird", "fat"]
    action_keywords = ["handle", "deal", "what do i do", "happening to me", "bullied", "being bullied"]
    
    if any(word in user_input for word in insults + action_keywords):
        return (
            "If someone is being mean to you, remember the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply. Don't give them the reaction they want.\n"
            "🚫 **BLOCK:** Use the app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, teacher, or counselor.\n\n"
            "**Important:** Take a screenshot for evidence before you block! 💜"
        )

    # --- LEVEL 3: CONTACTS & HELPLINES ---
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact", "talk to"]):
        return (
            "You don't have to deal with this alone. **Talk to these people:**\n\n"
            "- **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.\n"
            "- **TOUCHline (Counselling):** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180\n\n"
            "These resources are safe and private for students. 📞"
        )

    # --- LEVEL 4: SUPPORTING FRIENDS ---
    if any(word in user_input for word in ["friend", "support", "upstander"]):
        return (
            "Being an **Upstander** is a superpower! 💜\n\n"
            "- **Check-in:** Send a private message to check if they are okay.\n"
            "- **Screenshot:** Help your friend save evidence.\n"
            "- **Report:** Don't like or share mean posts—report them instead.\n"
            "- **Accompany:** Offer to walk with them to see a teacher."
        )

    # --- LEVEL 5: DEFAULT ---
    return "That's an important point for our booth! We are advocating for a safer school internet. How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("### VIA Project: Advocate for Digital Kindness")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! 💜 Ask me 'What is Cyberbullying?' or 'How do I handle a bully?'"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Ask about help, friends, or kindness..."):
    if not check_safety(prompt):
        st.error("🚫 **Safety Alert:** Please use respectful language. We promote kindness here.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        bot_response = get_bot_response(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
