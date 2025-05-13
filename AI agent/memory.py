import json

def save_chat(history, filename="chat_history.json"):
    with open(filename, "w") as f:
        json.dump(history, f)

def load_chat(filename="chat_history.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [{"role": "system", "content": "You are a helpful assistant."}]
