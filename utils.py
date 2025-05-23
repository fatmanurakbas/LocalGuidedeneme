import json
import os

DATA_FILE = "app_data/user_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"bookmarks": [], "likes": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_to_bookmarks(item):
    data = load_data()
    if item not in data["bookmarks"]:
        data["bookmarks"].append(item)
        save_data(data)

def add_to_likes(item):
    data = load_data()
    if item not in data["likes"]:
        data["likes"].append(item)
        save_data(data)


