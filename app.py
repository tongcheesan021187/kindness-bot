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

# --- 3. THE "PERFECT PRIORITY" BRAIN ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # --- TOPIC 1: ACTS OF CYBERKINDNESS ---
    # We check for KINDNESS first so it isn't confused with bullying acts.
    if "cyberkindness" in user_input:
        return (
            "**Cyberkindness** is all about making the internet a better place! 🌈\n\n"
            "Some common **acts of cyberkindness** include:\n"
            "1. **The Private Check-in:** Messaging a friend who was treated meanly to see if they are okay.\n"
            "2. **Reporting, Not Sharing:** Reporting a hurtful post instead of 'liking' or forwarding it.\n"
            "3. **Positive Posting:** Leaving encouraging comments on a classmate's work or photo.\n"
            "4. **Being an Upstander:** Politely speaking up in a group chat when someone is being excluded.\n"
            "5. **Inclusive Gaming:** Inviting the 'new kid' to join your squad or team chat."
        )

    # --- TOPIC 2: ACTS OF CYBERBULLYING ---
    if any(word in user_input for word in ["acts", "examples", "types"]) and "bullying" in user_input:
        return (
            "Cyberbullying takes many forms. Common **acts** include:\n"
            "1. **Harassment:** Sending mean or threatening messages repeatedly.\n"
            "2. **Exclusion:** Intentionally leaving someone out of group chats.\n"
            "3. **Outing:** Sharing someone's private secrets or photos without permission.\n"
            "4. **Flaming:** Starting online fights with offensive language.\n"
            "5. **Impersonation:** Making fake profiles to mock someone."
        )

    # --- TOPIC 3: EMERGENCY ADVICE (Stop, Block, Tell) ---
    emergency_keywords = ["handle", "deal", "victim", "help me", "ugly", "stupid", "idiot", "loser", "bully", "bullied"]
    if any(word in user_input for word in emergency_keywords):
        return (
            "If someone is being mean to you online, follow **STOP, BLOCK, TELL**:\n\n"
            "✋ **STOP:** Do not reply. Don't give them a reaction.\n"
            "🚫 **BLOCK:** Use app settings to block them immediately.\n"
            "🗣️ **TELL:** Show the messages to a trusted adult, teacher, or counselor.\n\n"
            "**Pro-tip:** Take a screenshot for evidence first! 💜"
        )

    # --- TOPIC 4: CONTACTS & HELPLINES ---
    if any(word in user_input for word in ["who", "call", "phone", "number", "helpline", "contact"]):
        return (
            "You don't have to deal with this alone. **Talk to:**\n"
            "- **In School:** Your Form Teacher or School Counselor.\n"
            "- **TOUCHline:** 1800 377 2252\n"
            "- **Care Corner Insight:** 6353 1180 📞"
        )

    # --- TOPIC 5: DEFINITIONS ---
    if "what is cyberbullying" in user_input:
        return (
            "**Cyberbullying** is using digital tools to repeatedly and intentionally hurt others. "
            "Remember: If you wouldn't say it to their face, don't type it! 🚫"
        )

    # DEFAULT
    return "That's an important point for our booth! How do you think we can help our classmates stay kind in our school chats?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome! 💜 Ask me 'What are some acts of cyberkindness?' or 'Who can I call for help?'"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Ask about kindness, acts, or help..."):
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
