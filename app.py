import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    # Only heavy vulgarities go here to keep the environment safe.
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
    
    # TOPIC 1: Victim Advice / Being Called Names (Stop-Block-Tell)
    insults = ["ugly", "stupid", "idiot", "dumb", "noob", "loser", "weird", "fat"]
    victim_keywords = ["victim", "bullied", "happening to me", "what do i do", "someone is mean"]
    if any(word in user_input for word in insults + victim_keywords):
        return (
            "I'm sorry you're dealing with this. Use the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply. Retaliation is what the bully wants.\n"
            "🚫 **BLOCK:** Use the app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, like a parent or teacher.\n\n"
            "**Pro-tip:** Always take a screenshot before you block them so you have evidence! 💜"
        )

    # TOPIC 2: Helplines (Who to call)
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact"]):
        return (
            "You don't have to deal with this alone. **Talk to:**\n\n"
            "- **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.\n"
            "- **TOUCHline (Counselling):** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180\n\n"
            "These resources are safe and private for students. 📞"
        )

    # TOPIC 3: Upstander (Supporting friends)
    if any(word in user_input for word in ["friend", "support", "upstander"]):
        return (
            "Being an **Upstander** is how we stop cyberbullying! 💜\n\n"
            "- **Check-in:** Send a private 'Are you okay?' message.\n"
            "- **Screenshot:** Help them save evidence.\n"
            "- **Report:** Don't like or share mean posts—report them instead.\n"
            "- **Accompany:** Offer to walk with them to see a teacher."
        )

    # TOPIC 4: What is Cyberbullying?
    if "what is cyberbullying" in user_input or ("define" in user_input and "bullying" in user_input):
        return (
            "**Cyberbullying** is using digital tools (like WhatsApp, TikTok, or Discord) to "
            "repeatedly and intentionally hurt or harass someone. It includes spreading rumors, "
            "posting hurtful photos, or excluding others. If you wouldn't say it to their "
            "face, don't type it on a screen! 🚫"
        )

    # TOPIC 5: What is Cyberkindness? (The missing piece!)
    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is the positive choice to make the internet a better place! 🌈\n\n"
            "It means being an Upstander, reporting meanness, and sending encouraging messages "
            "to classmates. It's about building a digital community where everyone feels safe."
        )

    # DEFAULT RESPONSE
    return "That's an important point for our booth! We are advocating for a safer school internet. How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("### VIA Project: Advocate for Digital Kindness")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! 💜 Ask me 'What is Cyberkindness?' or 'How do I handle a bully?'"}
    ]

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
