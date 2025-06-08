import os
import requests

# === OFFLINE Krishna-style Moral Reflections ===
moral_fallbacks = {
    "grief": "Even in sorrow, hold on to your dharma. Time heals when faith stands firm.",
    "fear": "Act without fear, for the outcome lies in the hands of the divine.",
    "doubt": "Clarity comes when you listen to your higher self in silence.",
    "anger": "Anger is fire, O seeker. Direct it into wisdom, not destruction.",
    "action": "Your right is to action alone, not the fruits. Begin without hesitation.",
    "ego": "Shed the idea of 'I'. Be the instrument, not the doer.",
    "loneliness": "Even when you feel alone, I am with you. Always.",
    "confusion": "When the path is unclear, silence will show the way.",
    "detachment": "Perform your duties, but remain unaffected by outcomes.",
    "purpose": "Purpose arises from inner alignment, not outer rewards.",
    "default": "Detach from results. Act righteously. Let dharma guide you."
}

# === OFFLINE Reflective Questions ===
reflective_questions = {
    "grief": "What memory is tied to this grief?",
    "fear": "What is the root of your fear?",
    "doubt": "What would clarity look like to you?",
    "anger": "What wound lies beneath this anger?",
    "action": "What can you do in this moment without fear?",
    "ego": "Are you acting to serve the self or the soul?",
    "loneliness": "What connection do you most deeply miss?",
    "confusion": "What is your heart whispering underneath the noise?",
    "detachment": "What are you holding onto that is holding you back?",
    "purpose": "If success was not measured by results, what would you do?",
    "default": "What are you truly seeking right now?"
}

# === OFFLINE: Krishna-style Advice ===
def generate_reflection(intent):
    return moral_fallbacks.get(intent, moral_fallbacks["default"])

# === OFFLINE: Introspective Question ===
def guiding_question(intent):
    return reflective_questions.get(intent, reflective_questions["default"])

# AI Implementation
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or "API_KEY"  # Replace with your OpenRouter API key
OPENROUTER_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

class ResponseGenerator:
    def __init__(self, api_key=OPENROUTER_API_KEY, model="gpt-4o-mini"):
        self.api_key = api_key
        self.model = model

    def generate_response(self, user_prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are KARM, an AI assistant inspired by Lord Krishna, providing wisdom and guidance."
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1000,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        try:
            response = requests.post(OPENROUTER_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            ai_message = data["choices"][0]["message"]["content"]
            return ai_message.strip()

        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"Error occurred: {err}"

# Wrapper function for backward compatibility:
def ai_response(prompt):
    gen = ResponseGenerator()
    return gen.generate_response(prompt)


# For quick local testing
if __name__ == "__main__":
    gen = ResponseGenerator()
    prompt = input("Enter your prompt for KARM: ")
    print("Response:", gen.generate_response(prompt))
