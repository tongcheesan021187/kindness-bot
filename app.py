import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    # These are the ONLY words that will trigger the "Safety Alert"
    # Add any specific severe vulgarities here that you want to block.
    blocked_words = ["insert_vulgarity_1", "insert_vulgarity_2"] 
    
    user_words = text.lower().split()
    for word in user_words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word in blocked_words:
            return False
    return True

# --- 3. THE UPGRADED KNOWLEDGE BASE ---
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    # Priority 1: Definitions
    if "what is cyberbullying" in user_input or "define cyberbullying" in user_input:
        return "Cyberbullying is repeated, mean behavior online using phones or computers. It includes spreading rumors, sending mean messages, or excluding people. It's never okay! 🚫"
    
    if "what is cyberkindness" in user_input or "define cyberkindness" in user_input:
        return "Cyberkindness is treating others online with the same respect you'd show them in person! It means being helpful, encouraging, and positive in comments and chats. 💜"

    # Priority 2: Specific Situations
    if "stupid" in user_input or "ugly" in user_input or "dumb" in user_input:
        return "Being called names hurts. Don't reply—that's what the person wants. Instead: 1. Take a screenshot, 2. Block them, and 3. Tell a teacher or parent. You are worth more than their words!"

    if "whatsapp" in user_input or "group chat" in user_input:
        return "Chat groups can get toxic. If a chat makes you feel bad, you have the right to mute it or leave. A real friend will understand your need for peace."

    if "report" in user_input:
        return "Reporting is not 'snitching'—it's staying safe. Use the 'Report' button on the app, or show the messages to your school counselor or CCE teacher."

    # Priority 3: General Advice
    if "help" in user_input or "tips" in user_input:
        return "I can help with: \n- Defining Cyberbullying \n- What to do if someone is mean \n- How to use the 'Stop, Block, Tell' rule."

    # Default Response if no keywords are found
    return "That's an interesting point. At our school, we promote being an 'Upstander' (someone who stands up for others). How do you think we can make our school chats Kinder?"

# --- 4. USER INTERFACE ---
st.title("💜 The CyberKindness Booth")
st.markdown("Welcome to our VIA Project! Type a question to learn how to keep our digital school space safe.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! 💜 Ask me something like 'What is cyberbullying?' or 'What do I do if someone is mean?'"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 5. CHAT LOGIC ---
if prompt := st.chat_input("Type here..."):
    if not check_safety(prompt):
        st.error("🚫 **Safety Alert:** We only use kind language at this booth. Please rephrase.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get the specific response using our logic function
        bot_response = get_bot_response(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
