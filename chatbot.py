import random

def detect_mood(text):
    text = text.lower()

    if any(word in text for word in ["sad", "depressed", "down", "unhappy"]):
        return "sad"
    elif any(word in text for word in ["stress", "tired", "anxious", "pressure"]):
        return "stress"
    elif any(word in text for word in ["happy", "good", "great", "excited"]):
        return "happy"
    else:
        return "neutral"

def get_response(user_input):
    mood = detect_mood(user_input)

    responses = {
        "sad": [
            "I’m really sorry you’re feeling this way 😔💙 You’re not alone.",
            "It’s okay to feel sad sometimes. I’m here with you 🫂",
            "Your feelings matter. Take a deep breath 🌱"
        ],
        "stress": [
            "That sounds stressful 😣 Take a slow breath with me.",
            "You’ve been strong for a long time — it’s okay to rest 💙",
            "One step at a time. You’re doing your best 🌸"
        ],
        "happy": [
            "That’s lovely to hear! 😊✨ Keep smiling.",
            "Your happiness made my day too 💛",
            "Yay! Let’s enjoy this moment 🌈"
        ],
        "neutral": [
            "I’m listening 💬 Tell me more.",
            "How has your day been so far? 🌼",
            "You can share anything here 💙"
        ]
    }

    return random.choice(responses[mood])
