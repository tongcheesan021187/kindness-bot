import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    # These are specific severe vulgarities you want to block.
    # Words like 'stupid' or 'ugly' are NOT in this list, so they are allowed.
    blocked_words = ["insert_extreme_vulgarity_1", "insert_extreme_vulgarity_2"] 
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
    if any(word in user_input for word in ["who", "help", "bullied", "counselor", "teacher", "advice"]):
        return """
        If you are facing online meanness, remember that you don't have to deal with it alone. 
        
        **Here is who you can talk to:**
        1. **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.
        2. **At Home:** Your parents, or an older sibling/cousin you trust.
        3. **Community Helplines (for Youth):** - **TOUCHline (Counselling):** 1800 377 2252
           - **Care Corner Insight:** 6353 1180
        
        It takes courage to speak up. Your safety and mental well-being are the priority! 💜
        """

    # RESPONSE FOR: "What is Cyberbullying?"
    if "cyberbullying" in user_input and ("what" in user_input or "define" in user_input):
        return """
        **Cyberbullying** is using digital platforms (like WhatsApp, TikTok, or Discord) to repeatedly 
        and intentionally hurt, embarrass, or harass someone. 
        
        It includes spreading rumors, posting hurtful photos, or creating groups to exclude others. 
        If you wouldn't say it to their face, don't type it on a screen! 🚫
        """

    # RESPONSE FOR: "Someone called me stupid/ugly/etc"
    if any(word in user_input for word in ["stupid", "ugly", "idiot", "dumb", "noob", "loser"]):
        return """
        I'm sorry someone was mean to you. It's important to remember: **Don't feed the trolls.** Bullies want a reaction. Try the **Stop, Block, Tell** method:
        1. **Stop:** Don't reply. 
        2. **Block:** Use the app settings to block them immediately.
        3. **Tell:** Show the messages to a trusted adult so they can help. 
        
        Their mean words don't change how awesome you are! ✨
        """

    # RESPONSE FOR: "What is Cyberkindness?"
    if "cyberkindness" in user_input:
        return """
        **Cyberkindness** is about making the internet a better place for everyone. 🌈
        
        It means:
        - Being an **Upstander** (defending someone being bullied).
        - Reporting hurtful content instead of sharing it.
        - Sending encouraging messages to classmates.
        Small acts of kindness can stop a lot of online hate!
        """

    # DEFAULT RESPONSE
    return "That's a great question for our booth! We are advocating for a kinder school community. How do you think we can help our classmates be more respectful in our school Telegram or WhatsApp groups?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("### VIA Project: Advocate for Digital Kindness")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to our booth! 💜 Ask me a question like 'Who can I ask for help?' or 'What is cyberbullying?'"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Ask about help, reporting, or definitions..."):
    if not check_safety(prompt):
        st.error("🚫 **Safety Alert:** We only use kind and respectful language here. Please rephrase.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        bot_response = get_bot_response(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
