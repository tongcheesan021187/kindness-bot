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

# --- 3. THE UPDATED BRAIN (Flexible Scanning) ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # RESPONSE FOR: Being called names (Ugly, Stupid, etc.)
    # This now checks if ANY of these words appear anywhere in the sentence
    insults = ["ugly", "stupid", "idiot", "dumb", "noob", "loser", "fat", "weird"]
    if any(word in user_input for word in insults):
        return (
            "I'm sorry someone said that to you. It's important to remember: **Don't feed the trolls.** "
            "Bullies want you to get angry or sad. Try the **Stop, Block, Tell** method:\n\n"
            "1. **Stop:** Don't reply. \n"
            "2. **Block:** Use the app settings to block them immediately.\n"
            "3. **Tell:** Show the messages to a teacher or parent. \n\n"
            "Their mean words don't change how awesome you are! ✨"
        )

    # RESPONSE FOR: Asking for help/Victim logic
    if any(word in user_input for word in ["victim", "bullied", "what do i do", "help me"]):
        return (
            "If you are facing online meanness, remember: It is NOT your fault. 💜\n\n"
            "1. **SAVE:** Take screenshots of everything as evidence.\n"
            "2. **BLOCK:** Block the person immediately so they can't send more.\n"
            "3. **TELL:** Talk to your Form Teacher, a CCE teacher, or the School Counselor.\n\n"
            "You can also call **TOUCHline at 1800 377 2252** for support."
        )

    # RESPONSE FOR: Supporting a friend
    if any(word in user_input for word in ["friend", "support", "upstander"]):
        return (
            "Being an **Upstander** is how we stop cyberbullying! 💜\n\n"
            "Check-in privately with your friend, help them take screenshots, and "
            "offer to walk with them to see a teacher during recess."
        )

    # RESPONSE FOR: Definitions
    if "cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital platforms to repeatedly hurt or harass someone. "
            "If you wouldn't say it to their face, don't type it on a screen! 🚫"
        )

    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is about making the internet better by being an Upstander "
            "and sending encouraging messages. 🌈"
        )

    # DEFAULT RESPONSE
    return "That's an important point for our booth! We are advocating for a safer school internet. How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("### VIA Project: Advocate for Digital Kindness")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! 💜 Ask me 'What if someone is mean to me?' or 'How can I support a friend?'"}
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
