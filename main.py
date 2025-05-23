import random
import json
import os
import hashlib

# ---- Banner ----
BANNER = [
    "███████████████████████████████████████████████████████████████████",
    "█─▄▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄─▄─█─▄▄─█─▄▄▄─█▄─██─▄█▄─▄▄─█─▄▄▄▄█─▄─▄─█",
    "█─███▀██─▄─▄██▄─▄███─▄▄▄███─███─██─█─██▀─██─██─███─▄█▀█▄▄▄▄─███─███",
    "▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀───▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀",
]

# ---- Configuration ----
SHIFT_LIST = [1, 3, 5, 7, 11]
KEYWORDS = ["APPLE", "BERRY", "CHERRY", "MANGO", "PEACH"]
PASSWORDS = ["SUN", "MOON", "STAR", "SKY", "CLOUD"]
HALL_FILE = "hall_of_heroes.json"
TOTAL_HINTS = 3
LEVEL_HINT_LIMIT = 2

# ---- Persistence ----
def load_hall():
    try:
        if os.path.exists(HALL_FILE):
            with open(HALL_FILE, "r") as f:
                return json.load(f)
    except OSError:
        print("[!] Warning: Could not read hall file; starting fresh.")
    except json.JSONDecodeError:
        print("[!] Warning: Hall file corrupted; resetting list.")
    return []

hall = load_hall()

def save_hall():
    try:
        with open(HALL_FILE, "w") as f:
            json.dump(hall, f)
    except OSError:
        print("[!] Warning: Could not save Hall of Heroes.")

# ---- Ciphers ----
def caesar_cipher(text, shift):
    result = ''
    for c in text:
        if c.isalpha():
            base = ord('A')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def vigenere_cipher(text, key):
    result = ''
    key = key.upper()
    ki = 0
    for c in text:
        if c.isalpha():
            base = ord('A')
            shift = ord(key[ki % len(key)]) - base
            result += chr((ord(c) - base + shift) % 26 + base)
            ki += 1
        else:
            result += c
    return result

def hash_lab(text, salt):
    return hashlib.sha256((text + salt).encode()).hexdigest().upper()

# ---- Helpers ----
def get_hint(level, answer, used_hints, hint_limit):
    if used_hints[level] >= hint_limit:
        print("[!] No more hints for this level.")
        return False
    used_hints[level] += 1
    if level == 1:
        print(f"[Hint] First letter: '{answer[0]}'")
    elif level == 2:
        print(f"[Hint] Key starts with: '{answer[0]}'")
    else:
        print(f"[Hint] Salt word: '{answer}'")
    return True

def show_help():
    print("\n=== Help Menu ===")
    print(" H - Get a hint")
    print(" A - Reveal answer (auto-fail level)")
    print(" ? - Show help menu")
    print(" Q - Quit game")
    print("=================\n")

def tutorial():
    print("=== Tutorial ===")
    print("1) Level 1: Caesar Shift — letters shift by a fixed number.")
    print("2) Level 2: Vigenere Cipher — shift varies by keyword letters.")
    print("3) Level 3: HashLab — match SHA-256 hash with salt word.")
    print(f"You have {TOTAL_HINTS} hints total, max {LEVEL_HINT_LIMIT} per level.")
    print("================\n")

# ---- Main Game ----
def play():
    # Print banner
    for line in BANNER:
        print(line)
    print("\n*** Welcome to CryptoQuest ***\n")
    show_help()
    tutorial()

    hints_used = 0
    level_hints = {1: 0, 2: 0, 3: 0}
    shift = random.choice(SHIFT_LIST)
    keyword = random.choice(KEYWORDS)
    password = random.choice(PASSWORDS)

    for level in (1, 2, 3):
        if level == 1:
            title, answer = 'Caesar Shift', keyword
            puzzle = caesar_cipher(answer, shift)
        elif level == 2:
            title, answer = 'Vigenere Cipher', keyword
            puzzle = vigenere_cipher(answer, password)
        else:
            title, answer = 'HashLab (SHA-256)', keyword
            puzzle = hash_lab(answer, password)

        print(f"--- Level {level}: {title} ---")
        while True:
            print(f"Puzzle: {puzzle}")
            cmd = input("Your input > ").strip().upper()
            if cmd == 'H':
                if hints_used < TOTAL_HINTS and get_hint(level, (password if level > 1 else answer), level_hints, LEVEL_HINT_LIMIT):
                    hints_used += 1
                continue
            if cmd == '?':
                show_help()
                continue
            if cmd == 'A':
                print(f"[!] Answer: '{answer}'. Moving on...\n")
                break
            if cmd == 'Q':
                print("Quitting game. Goodbye!")
                return
            if cmd == answer:
                print("[+] Correct!\n")
                break
            print("[-] Wrong, try again.")
        print("---------------------\n")

    xp = random.randint(90, 140)
    print(f"*** You earned {xp} XP! ***")
    player = input("Enter your name for the Hall of Heroes > ").strip()
    hall.append({'name': player, 'xp': xp})
    save_hall()

    print("\n=== Hall of Heroes ===")
    for entry in hall:
        print(f"{entry['name']}: {entry['xp']} XP")
    print("======================")

if __name__ == "__main__":
    play()
