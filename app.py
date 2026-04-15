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

# --- 3. THE "ALL-IN-ONE" BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # CATEGORY A: WHO TO CALL / HELPLINES
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact"]):
        return (
            "You don't have to deal with this alone. **Here are people you can contact:**\n\n"
            "1. **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.\n"
            "2. **Professional Helplines (for Youth):**\n"
            "   - **TOUCHline (Counselling):** 1800 377 2252\n"
            "   - **Care Corner Insight:** 6353 1180\n"
            "3. **Emergency:** If you feel you are in immediate danger, tell a parent or call 999.\n\n"
            "Speaking up is the first step to staying safe! 💜"
        )

    # CATEGORY B: INSULTS (Ugly, Stupid, etc.)
    insults = ["ugly", "stupid", "idiot", "dumb", "noob", "loser", "weird"]
    if any(word in user_input for word in insults):
        return (
            "I'm sorry someone was mean. Remember the **Stop, Block, Tell** method:\n"
            "1. **Stop:** Don't reply. They want a reaction!\n"
            "2. **Block:** Use app settings to block them immediately.\n"
            "3. **Tell:** Show the messages to a teacher or parent.\n\n"
            "Their mean words don't change how awesome you are! ✨"
        )

    # CATEGORY C: VICTIM ADVICE (What do I do?)
    if any(word in user_input for word in ["victim", "bullied", "happening to me", "what do i do"]):
        return (
            "If you are being bullied, it is NOT your fault. 💜\n\n"
            "1. **SAVE:** Take screenshots of the messages and the person's profile.\n"
            "2. **BLOCK:** Cut off their access to you immediately.\n"
            "3. **TELL:** Reach out to a teacher or counselor. Reporting is brave!"
        )

    # CATEGORY D: UPSTANDER (Helping a friend)
    if any(word in user_input for word in ["friend", "support", "upstander"]):
        return (
            "Being an **Upstander** is how we stop cyberbullying! 💜\n\n"
            "- Check-in privately: 'Are you okay?'\n"
            "- Help them take screenshots as evidence.\n"
            "- Offer to walk with them to see a teacher during recess.\n"
            "- Don't join in or 'like' the mean posts."
        )

    # CATEGORY E: DEFINITIONS
    if "cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools to repeatedly hurt or harass someone. "
            "If you wouldn't say it to their face, don't type it on a screen! 🚫"
        )

    # DEFAULT RESPONSE
    return "That's an important point for our booth! We are advocating for a safer school internet. How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("### VIA Project: Advocate for Digital Kindness")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! 💜 Ask me 'Who can I call for help?' or 'What if someone is mean to me?'"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Ask about helplines, friends, or advice..."):
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
