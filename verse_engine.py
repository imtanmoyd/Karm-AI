import json

with open("gita_db.json", encoding='utf-8') as f:
    GITA_DB = json.load(f)

def get_shloka(intent):
    matches = [v for v in GITA_DB if v.get("theme") == intent]
    return matches[0] if matches else None
