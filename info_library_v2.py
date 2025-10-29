#!/usr/bin/env python3
import json, sys, os, datetime

DATA_FILE = os.path.expanduser("~/immutable-gdscript-framework/info_library_data.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_entry(category, title, content):
    data = load_data()
    if category not in data:
        data[category] = []
    data[category].append({
        "title": title,
        "content": content,
        "timestamp": datetime.datetime.now().isoformat()
    })
    save_data(data)
    print(f"✅ Added '{title}' under category '{category}'")

def list_all():
    data = load_data()
    if not data:
        print("No entries yet.")
        return
    print("=== All Categories ===")
    for cat, entries in data.items():
        print(f"- {cat} ({len(entries)} items)")

def list_category(category):
    data = load_data()
    if category not in data:
        print(f"No such category: {category}")
        return
    print(f"=== Entries in '{category}' ===")
    for e in data[category]:
        print(f"- {e['title']} ({e['timestamp']})")

def view_entry(category, title):
    data = load_data()
    if category not in data:
        print(f"No such category: {category}")
        return
    for e in data[category]:
        if e["title"] == title:
            print(f"📖 {e['title']} ({e['timestamp']})\n{'-'*40}\n{e['content']}")
            return
    print(f"No entry titled '{title}' in '{category}'")

def delete_entry(category, title):
    data = load_data()
    if category not in data:
        print(f"No such category: {category}")
        return
    data[category] = [e for e in data[category] if e["title"] != title]
    save_data(data)
    print(f"🗑️ Deleted '{title}' from '{category}'")

def main():
    if len(sys.argv) < 2:
        print("Usage: info_library_v2.py [add|list|view|delete] ...")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "add" and len(sys.argv) >= 5:
        add_entry(sys.argv[2], sys.argv[3], " ".join(sys.argv[4:]))
    elif cmd == "list":
        if len(sys.argv) == 2:
            list_all()
        else:
            list_category(sys.argv[2])
    elif cmd == "view" and len(sys.argv) == 4:
        view_entry(sys.argv[2], sys.argv[3])
    elif cmd == "delete" and len(sys.argv) == 4:
        delete_entry(sys.argv[2], sys.argv[3])
    else:
        print("Invalid command or arguments.")

if __name__ == "__main__":
    main()
