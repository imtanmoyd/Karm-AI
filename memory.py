import json
from pathlib import Path
from datetime import datetime

MEMORY_FILE = Path("memory_log.json")

def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"history": []}

def save_prompt(prompt, result=None, shloka=None):
    memory = load_memory()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build shloka block only if valid
    shloka_info = None
    if shloka and isinstance(shloka, dict) and shloka.get("chapter") and shloka.get("verse"):
        shloka_info = {
            "chapter": shloka.get("chapter"),
            "verse": shloka.get("verse"),
            "text": shloka.get("shloka"),
            "translation": shloka.get("translation"),
            "theme": shloka.get("theme")
        }

    entry = {
        "timestamp": now,
        "prompt": prompt.strip(),
        "response": result.strip() if result else None,
        "shloka": shloka_info
    }

    memory["history"].append(entry)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def get_memory():
    return load_memory()["history"]
