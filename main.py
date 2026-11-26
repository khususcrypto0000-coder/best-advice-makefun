import os

ENTRY = "My dad said never borrow money to look rich, because the people you're trying to impress are probably in debt too."

def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be whitespace only"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
