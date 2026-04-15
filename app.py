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

# --- 3. THE UPDATED BRAIN (With Priority Logic) ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # PRIORITY 1: Help for Victims (If they ask "what do I do" or "I am being...")
    if any(word in user_input for word in ["victim", "happening to me", "i am bullied", "i am being", "what do i do"]):
        return (
            "If this is happening to you, remember: It is NOT your fault. 💜\n\n"
            "1. **STOP:** Do not reply. Retaliation gives them the reaction they want.\n"
            "2. **SAVE:** Take screenshots of everything as evidence (messages and profile).\n"
            "3. **BLOCK:** Use the app settings to block the person immediately.\n"
            "4. **TELL:** Show the evidence to a teacher, counselor, or parent. "
            "You can also call TOUCHline at 1800 377 2252 for support."
        )

    # PRIORITY 2: Help for Friends (Upstander logic)
    if any(word in user_input for word in ["friend", "support", "upstander"]):
        return (
            "Being an **Upstander** is how we stop cyberbullying! 💜\n\n"
            "1. **Check-in Privately:** Send a DM saying 'I saw what happened, are you okay?'\n"
            "2. **Don't Engage:** Don't like or reply to the bully.\n"
            "3. **Help with Evidence:** Remind your friend to take **screenshots**.\n"
            "4. **Accompany Them:** Offer to go with them to talk to a teacher.\n"
            "5. **Be a Buffer:** Change the subject in a toxic group chat."
        )

    # PRIORITY 3: General Help/Resources
    if any(word in user_input for word in ["who", "help", "counselor", "teacher"]):
        return (
            "You don't have to deal with this alone. **Talk to:**\n\n"
            "- **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.\n"
            "- **At Home:** Your parents or an older sibling you trust.\n"
            "- **Community Helplines:** \n"
            "  - TOUCHline (Counselling): 1800 377 2252\n"
            "  - Care Corner Insight: 6353 1180"
        )

    # PRIORITY 4: Definitions (Only if not asking for help)
    if "cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital platforms to repeatedly hurt or harass someone. "
            "It includes spreading rumors, posting hurtful photos, or excluding others from groups. "
            "If you wouldn't say it to their face, don't type it on a screen! 🚫"
        )

    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is about making the internet better! 🌈\n\n"
            "It means being an Upstander, reporting hurtful content, and sending "
            "encouraging messages. Small acts of kindness stop a lot of online hate!"
        )

    # DEFAULT RESPONSE
    return "That's a great question! At this booth, we're promoting digital safety. How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("### VIA Project: Advocate for Digital Kindness")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! 💜 Ask me 'What do I do if I'm bullied?' or 'How can I support a friend?'"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Type here..."):
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
