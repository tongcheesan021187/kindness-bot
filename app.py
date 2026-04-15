import streamlit as st

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. THE CUSTOM SAFETY FILTER ---
def check_safety(text):
    # These are specific severe vulgarities you want to block.
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
    
    # RESPONSE FOR: "How can I help/support my friend?"
    if any(word in user_input for word in ["friend", "support", "help someone", "upstander"]):
        return """
        Being a supportive friend (an **Upstander**) is how we stop cyberbullying! Here is what you can do:
        
        1. **Check-in Privately:** Send them a DM saying "I saw what happened, are you okay?" It means a lot.
        2. **Don't Engage:** Don't like or reply to the bully. It just gives them more attention.
        3. **Help with Evidence:** Remind your friend to take **screenshots** before they delete the chat.
        4. **Accompany Them:** Offer to go with them to talk to a teacher or counselor during recess.
        5. **Be a Buffer:** Try to change the subject in a toxic group chat to stop the meanness.
        
        You are making a difference just by being there for them! 💜
        """

    # RESPONSE FOR: "Who do I ask for help?" (General)
    if any(word in user_input for word in ["who", "help", "bullied", "counselor", "teacher", "advice"]):
        return """
        If you are facing online meanness, remember that you don't have to deal with it alone. 
        
        **Here is who you can talk to:**
        - **In School:** Your Form Teacher, a CCE teacher, or the School Counselor.
        - **At Home:** Your parents, or an older sibling/cousin you trust.
        - **Community Helplines:** - **TOUCHline (Counselling):** 1800 377 2252
          - **Care Corner Insight:** 6353 1180
        
        It takes courage to speak up. Your safety is the priority!
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
        I'm sorry someone was mean to you. Try the **Stop, Block, Tell** method:
        1. **Stop:** Do not reply to the bully. 
        2. **Block:** Use the app settings to block them immediately.
        3. **Tell:** Show the
