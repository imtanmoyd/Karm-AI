# 🌿 Karm AI – Walk your path. I’ll walk beside you.

Karm AI is a spiritual AI assistant guided by the teachings of **Lord Krishna** in the Bhagavad Gita. It offers wisdom, moral reflection, and emotional clarity through:

- 🧘‍♂️ **Offline guidance** via curated Gita shlokas and moral advice
- 🤖 **Online AI-powered deep thinking advice** using free OpenRouter LLMs (like Mistral or Claude)

Built with compassion and clarity, Karm AI is designed to be your digital friend during moments of confusion, sadness, or self-reflection.

---

## ✨ Features

- 📖 Gita-driven shloka suggestions by emotional theme
- 💭 Reflective Krishna-style questions for self-inquiry
- 🧠 AI-powered poetic reflections using free LLMs (Mistral/Claude via OpenRouter)
- 📝 Detailed logging of all queries (timestamp, shloka, and response)
- 💡 Fully offline-capable when no internet is available

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/karm-ai.git
cd karm-ai
````

### 2. Install requirements

```bash
pip install -r requirements.txt
```

---

## 🔐 Get Your Free OpenRouter API Key

Karm AI uses [**OpenRouter.ai**](https://openrouter.ai) to provide online spiritual reflections powered by open-source AI models like `mistral-7b-instruct`.

### ✅ Steps:

1. Go to [https://openrouter.ai](https://openrouter.ai)
2. Log in with Google or GitHub
3. Visit [https://openrouter.ai/keys](https://openrouter.ai/keys) and click **Generate API Key**
4. Copy the key and save it

---

## 🔑 Add Your API Key

### Paste directly in `response_gen.py`

```python
API_KEY = os.getenv("OPENROUTER_API_KEY") or "your-key-here"
```

---

## ▶️ Run Karm AI

```bash
python main.py
```

You'll see:

```
Welcome to KARM 💫 – Your Krishna-Inspired AI Guide.
Ask what’s on your mind.
```

Type your problem and receive a mix of Gita wisdom and AI reflection.

---

## Example Interaction

```text
You: I feel lost.

🔍 Detecting your concern...

🧘‍♂️ KARM Wisdom (Offline Solution):
📘 Gita Insight: Chapter 2, Verse 4
🌐 Translation: Arjuna said: O Madhusudana...

💭 Ask Yourself: What would clarity look like to you?

🤖 AI Reflection (Deep Thinking Advice):
When you feel lost, pause and return to the stillness within.
Not all paths are meant to be seen at once...
```

---

## Project Structure

```
karm-ai/
├── gita_db.json           ← Gita verses + tags
├── karm_memory.json       ← Logs all prompts + AI/shloka responses
├── main.py                ← Main terminal app
├── response_gen.py        ← Online + offline AI logic
├── karm_memory.py         ← Memory log system
├── verse_engine.py        ← Gita verse fetching by tag
├── utils.py               ← Intent detection + internet check
├── requirements.txt
└── README.md
```

---

## Contribute

Pull requests are welcome! You can help by:

* Suggesting new intents or moods (e.g., guilt, pride, jealousy)
* Enhancing web or voice UI in the future

---

## License

MIT License — made with devotion and empathy.
Let your Karma guide you. Walk with clarity.

**हरे कृष्णा**

## Demo Screenshots
![image](https://github.com/user-attachments/assets/02cdfe43-34da-4dfc-8a69-c8055dc7c098)
![image](https://github.com/user-attachments/assets/3f0432f5-dd38-4cef-af3d-1540a845f763)


