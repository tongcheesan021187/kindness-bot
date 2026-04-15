import streamlit as st
from better_profanity import profanity

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="CyberKindness Booth", page_icon="💜")

# --- 2. SAFETY FILTER SETUP ---
# We initialize the filter to block vulgarities but allow school-level insults 
# so the bot can actually discuss them and give helpful advice.
if 'filter_ready' not in st.session_state:
    profanity.load_censor_words()
    # List of words we want the bot to ALLOW so it can talk about them
    allowed = {"stupid", "ugly", "idiot", "dumb", "noob", "loser", "shut up"}
    # Create a new list that doesn't include the allowed words
    custom_bad_words = [w for w in profanity.CENSOR_WORDSET if w not in allowed]
    profanity.load_censor_words(custom_bad_words)
    st.session_state['filter_ready'] = True

def check_safety(text):
    """Returns True if the message is clean of serious vulgarities."""
    return not profanity.contains_profanity(text)

# --- 3. THE KNOWLEDGE BASE ---
# These are the triggers for your booth visitors
knowledge = {
    "what is": "Cyberkindness is treating others online with the same respect you'd show them in person! 💜",
    "cyberbullying": "Cyberbullying is repeated, mean behavior online. Remember: It's not your fault. Stop, Block, and Tell a trusted adult.",
    "stupid": "Being called names like 'stupid' hurts. Don't reply—that's what the bully wants. Take a screenshot and talk to a teacher or counselor.",
    "ugly": "If someone calls you names like 'ugly', remember that their behavior says more about them than it does about you. Block them and move on!",
    "mean": "If someone is being mean, use the 'Stop, Block, Tell' rule. Don't let their pixels ruin your day!",
    "report": "Most apps (IG, TikTok, WhatsApp) have a 'Report' button. In school, your CCE teacher or counselor is always here to help.",
    "anonymous": "Being anonymous isn't a license to be mean. Digital footprints are real and lasting!",
    "whatsapp": "Chat groups can get toxic. You have the right to mute or leave any group that makes you feel unsafe.",
    "help": "I can help with: \n1. Dealing with insults \n2
