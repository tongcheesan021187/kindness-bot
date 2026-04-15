# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Welcome to the CyberKindness Booth! 💜 I'm here to help you learn about being a great friend online. You can ask me 'What is cyberbullying?' or tell me about a situation you've seen."
        }
    ]
        
        with st.chat_message("assistant"):
            st.markdown(found_reply)
            st.session_state.messages.append({"role": "assistant", "content": found_reply})
