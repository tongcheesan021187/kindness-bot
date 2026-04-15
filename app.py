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

# --- 3. THE IMPROVED BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # --- CATEGORY 1: HANDLING A BULLY / VICTIM ADVICE ---
    # This now catches "handle", "deal", "bully", "mean", and "what do I do"
    victim_triggers = ["handle", "deal", "bully", "victim", "mean", "what do i do", "happening to me", "bullied"]
    insults = ["ugly", "stupid", "idiot", "dumb", "noob", "loser", "weird", "fat"]
    
    if any(word in user_input for word in victim_triggers + insults):
        return (
            "If someone is being a bully, you have the power to stop the situation. "
            "Follow the **STOP, BLOCK, TELL** method:\n\n"
            "✋ **STOP:** Do not reply or argue. Bullies want a reaction—don't give them one.\n"
            "🚫 **BLOCK:** Use the app settings to block them immediately. You don't have to listen to meanness.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, like your Form Teacher, a parent, or a counselor.\n\n"
            "**Important:** Take a screenshot of the messages before you block them so you have evidence! 💜"
        )

    # --- CATEGORY 2: WHO TO CALL (Helplines) ---
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact", "talk to"]):
        return (
            "You don't have to deal with this alone. **Talk to these people:**\n\n"
            "- **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.\n"
            "- **TOUCHline (Counselling):** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180\n\n"
            "These resources are safe, private, and meant for students like you. 📞"
        )

    # --- CATEGORY 3: SUPPORTING FRIENDS (Upstander) ---
    if any(word in user_input for word in ["friend", "support", "upstander", "help them"]):
        return (
            "Being an **Upstander** is a superpower! 💜\n\n"
            "- **Reach out:** Send a private message to check if they are okay.\n"
            "- **Don't join in:** Don't like or share the mean post.\n"
            "- **Evidence:** Help your friend take screenshots.\n"
            "- **Report:** Report the post to the app and tell a teacher."
        )

    # --- CATEGORY 4: DEFINITIONS ---
    if "cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools to repeatedly and intentionally hurt others. "
            "It can happen on WhatsApp, Telegram, TikTok, or in games. "
            "If you wouldn't say it to their face, don't type it! 🚫"
        )

    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is choosing to be positive online! 🌈\n\n"
            "It's about being an Upstander, reporting meanness, and sending "
            "encouraging messages to make our school digital space safe for everyone."
        )

    # --- DEFAULT RESPONSE ---
    return "That's an interesting point. At our booth, we believe in being 'Upstanders'. How do you think we can make our school chats Kinder?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("### VIA Project: Advocate for Digital Kindness")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! 💜 Ask me 'How do I handle a bully?' or 'Who can I call for help?'"}
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
