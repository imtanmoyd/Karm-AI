from textblob import TextBlob
import socket

INTENT_KEYWORDS = {
    "grief": ["sad", "miss", "cry", "heart", "pain", "love"],
    "fear": ["afraid", "fear", "worry", "exam", "fail", "future"],
    "doubt": ["confused", "uncertain", "lost"],
    "anger": ["angry", "mad", "annoyed"],
    "action": ["what to do", "next step", "stuck"],
}

def detect_intent(prompt):
    prompt = prompt.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        for word in keywords:
            if word in prompt:
                return intent
    # Fallback to sentiment
    polarity = TextBlob(prompt).sentiment.polarity
    if polarity < -0.3:
        return "grief"
    elif polarity > 0.3:
        return "action"
    return "doubt"

def has_internet():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=2)
        return True
    except OSError:
        return False
