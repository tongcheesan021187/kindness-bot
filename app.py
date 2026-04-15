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

# --- 3. THE RE-PRIORITIZED BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # --- PRIORITY 1: SUPPORTING A FRIEND (Upstander Logic) ---
    # We check this first so the bot doesn't assume YOU are the one being bullied.
    if any(word in user_input for word in ["friend", "someone else", "support", "upstander", "help a"]):
        return (
            "Being an **Upstander** is a superpower! 💜 Here is how you can help your friend:\n\n"
            "1. **Check-in Privately:** Send a DM or talk to them in person. Ask, 'I saw what happened, are you okay?'\n"
            "2. **Don't Engage:** Do not reply to the bully or 'like' the mean posts. This stops the drama from spreading.\n"
            "3. **Help with Evidence:** Remind your friend to take **screenshots** before they block the person.\n"
            "4. **Accompany Them:** Offer to go with them to talk to a teacher, counselor, or parent.\n"
            "5. **Be a Buffer:** Start a positive conversation in the group chat to shift the focus away from the meanness."
        )

    # --- PRIORITY 2: ACTS AND EXAMPLES ---
    if any(word in user_input for word in ["acts", "examples", "types", "looks like"]):
        if "kindness" in user_input:
            return (
                "**Acts of Cyberkindness** make the internet better! 🌈\n\n"
                "1. **Checking In:** Private messaging someone who was bullied.\n"
                "2. **Reporting:** Flagging mean content instead of sharing it.\n"
                "3. **Including:** Inviting someone who is left out into a chat.\n"
                "4. **Positive Comments:** Leaving encouraging words on a post."
            )
        return (
            "Cyberbullying acts include: **Harassment** (mean messages), **Exclusion** (leaving people out), "
            "**Outing** (sharing secrets), and **Impersonation** (fake profiles). ✋"
        )

    # --- PRIORITY 3: DEFINITIONS ---
    if "what is cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools to repeatedly and intentionally hurt others. "
            "If you wouldn't say it to their face, don't type it! 🚫"
        )

    # --- PRIORITY 4: EMERGENCY ADVICE (For the User) ---
    emergency_keywords = ["handle", "deal", "victim", "help me", "ugly", "stupid", "idiot", "loser", "bully", "bullied"]
    if any(word in user_input for word in emergency_keywords) or user_input.startswith("how"):
        return (
            "If someone is being mean to you online, follow the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply. Don't give them a reaction.\n"
            "🚫 **BLOCK:** Use app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, teacher, or counselor.\n\n"
            "**Pro-tip:** Take a screenshot for evidence first! 💜"
        )

    # --- PRIORITY 5: HELPLINES ---
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
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! 💜 Ask me 'How can I support a friend?' or 'What is cyberbullying?'"}]

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
