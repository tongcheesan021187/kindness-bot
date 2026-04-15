import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    # Add any specific severe vulgarities here you want to block
    blocked_words = ["insert_vulgarity_1", "insert_vulgarity_2"] 
    user_words = text.lower().split()
    for word in user_words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word in blocked_words:
            return False
    return True

# --- 3. THE ADVANCED BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # RESPONSE FOR: "Who do I ask for help?"
    if any(word in user_input for word in ["who", "help", "bullied", "counselor", "teacher"]):
        return """
        If you are being bullied, you are not alone. Here is **who you can talk to right now**:
        1. **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.
        2. **At Home:** Your parents or an older sibling you trust.
        3. **Helplines:** You can call the **Tinkle Friend** (1800 274 4788) or **HELP123** (1800 612 3123).
        Remember: Reporting is the brave thing to do! 💜
        """

    # RESPONSE FOR: "What is Cyberbullying?"
    if "cyberbullying" in user_input and ("what" in user_input or "define" in user_input):
        return "Cyberbullying is using digital tools to intentionally hurt or humiliate others. This includes sending mean texts, sharing private photos without permission, or spreading rumors in group chats. It is a serious issue that we can stop together."

    # RESPONSE FOR: "Someone called me stupid/ugly"
    if any(word in user_input for word in ["stupid", "ugly", "idiot", "dumb", "noob"]):
        return "I'm sorry that happened. People often use mean words because they want a reaction. **Don't give it to them.** Screenshot the message, block their account, and tell a trusted adult. Their mean comment says nothing about your true value! ✨"

    # RESPONSE FOR: "What is Cyberkindness?"
    if "cyberkindness" in user_input:
        return "Cyberkindness is the 'opposite' of bullying. It's using your keyboard to lift people up! Like defending a friend in a chat, reporting a mean post, or just sending a 'Good Luck' message before an exam. 🌈"

    # RESPONSE FOR: "How to report?"
    if "report" in user_input:
        return "Most apps (Instagram, TikTok, WhatsApp) have a 'Report' button. Press it! It sends the message to the app developers. For school-related issues, always show the evidence to a teacher so they can help you resolve it safely."

    # DEFAULT RESPONSE
    return "That's a good question. At this booth, we're advocating for a safer school internet. Do you think we should have stricter rules for school WhatsApp groups?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("### Real-Time Support & Advocacy")
st.info("This bot is part of our VIA project. Type your questions below to learn about digital safety.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm here to help you stay safe online. What's on your mind today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Ask me about help, definitions, or reporting..."):
    if not check_safety(prompt):
        st.error("🚫 **Safety Alert:** Please use kind language. We promote respect at this booth.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate specific response
        bot_response = get_bot_response(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
