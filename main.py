import random
import json
import os
import hashlib
import sys

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
QUESTION_BASE_SCORE = 100

# ---- Persistence ----
def load_hall():
    try:
        if os.path.exists(HALL_FILE):
            with open(HALL_FILE, "r") as f:
                return json.load(f)
    except (OSError, json.JSONDecodeError):
        print("[!] Could not load Hall of Heroes; starting fresh.")
    return []

hall = load_hall()

def save_hall():
    try:
        with open(HALL_FILE, "w") as f:
            json.dump(hall, f)
    except OSError:
        print("[!] Could not save Hall of Heroes.")

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
            s = ord(key[ki % len(key)]) - base
            result += chr((ord(c) - base + s) % 26 + base)
            ki += 1
        else:
            result += c
    return result


def hash_lab(text, salt):
    return hashlib.sha256((text + salt).encode()).hexdigest().upper()

# ---- Helpers ----
def get_hint(level, secret, used, limit, shift_val=None):
    if used[level] >= limit:
        print("[!] No more hints for this level.")
        return False
    used[level] += 1
    if used[level] == 1:
        if level == 1 and shift_val is not None:
            print(f"[Hint] Shift value is {shift_val}")
        else:
            print(f"[Hint] First letter of secret: '{secret[0]}'")
    elif used[level] == 2:
        letter = random.choice(secret)
        print(f"[Hint] Random letter from secret: '{letter}'")
    return True


def show_help():
    print("\n=== Help Menu ===")
    print(" H - Get a hint (reduces this question's points)")
    print(" A - Reveal answer (fail level, -50 points)")
    print(" ? - Show this help menu")
    print(" Q - Quit to main menu")
    print("=================")


def tutorial():
    print("\n=== Tutorial ===")
    print("• Each question is worth 100 points.")
    print("• 1st hint: question score ×0.5")
    print("• 2nd hint: question score ×0.25")
    print("• Reveal (A): earn 0, total score -50")
    print(f"• Total hints: {TOTAL_HINTS}, max {LEVEL_HINT_LIMIT} per level.")
    print("================")


def show_credits():
    print("\n=== Credits ===")
    print(f"{'Author':<12}: Güneş Yılmaz")
    print(f"{'Instructor':<12}: Hicabi Yeniay")
    print(f"{'Course':<12}: AP CSP")
    print("================")


def show_hall():
    print("\n=== Hall of Heroes ===")
    if not hall:
        print(" No entries yet.")
    else:
        sorted_hall = sorted(hall, key=lambda e: e.get('score', e.get('xp',0)), reverse=True)
        medals = ['🥇', '🥈', '🥉']
        for i, entry in enumerate(sorted_hall):
            medal = medals[i] if i < 3 else '   '
            score = entry.get('score', entry.get('xp',0))
            print(f" {medal} {entry.get('name','?'):12} : {score}")
    print("================\n")

# ---- Game Logic ----
def play():
    total_score = 0
    hints_used_global = 0
    used_hints = {1: 0, 2: 0, 3: 0}

    for level in (1, 2, 3):
        base = QUESTION_BASE_SCORE
        shift_val = None
        if level == 1:
            shift_val = random.choice(SHIFT_LIST)
            answer = random.choice(KEYWORDS)
            puzzle = caesar_cipher(answer, shift_val)
            secret = answer
            title = "Caesar Shift"
        elif level == 2:
            answer = random.choice(KEYWORDS)
            key = random.choice(PASSWORDS)
            puzzle = vigenere_cipher(answer, key)
            secret = key
            title = "Vigenere Cipher"
        else:
            answer = random.choice(KEYWORDS)
            salt = random.choice(PASSWORDS)
            puzzle = hash_lab(answer, salt)
            secret = salt
            title = "HashLab (SHA-256)"

        print(f"--- Level {level}: {title} ---")
        print(f" Puzzle: {puzzle}")
        revealed = False
        while True:
            cmd = input("Your input > ").strip().upper()
            if cmd == 'H':
                if hints_used_global < TOTAL_HINTS and get_hint(level, secret, used_hints, LEVEL_HINT_LIMIT, shift_val):
                    hints_used_global += 1
                continue
            if cmd == '?':
                show_help()
                continue
            if cmd == 'A':
                print(f"[!] Answer: {answer}\n")
                total_score -= 50
                revealed = True
                break
            if cmd == 'Q':
                print("[!] Exiting to menu...\n")
                return total_score
            if cmd == answer:
                print("[+] Correct!\n")
                break
            print("[-] Wrong, try again.")

        if not revealed:
            used = used_hints[level]
            if used == 0:
                pts = base
            elif used == 1:
                pts = base // 2
            else:
                pts = base // 4
            total_score += pts
        print(f" Score after level {level}: {total_score}\n")

    print(f"*** Final Score: {total_score} ***\n")
    name = input("Your name for Hall of Heroes > ").strip()
    hall.append({'name': name, 'score': total_score})
    save_hall()
    return total_score

# ---- Main Menu ----
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in BANNER:
            print(line)
        print("\nCryptoQuest Menu:\n")
        print("1) Play")
        print("2) Help")
        print("3) Hall of Heroes")
        print("4) Credits")
        print("5) Save & Quit\n")
        choice = input("Select an option > ").strip()
        if choice == '1':
            play()
            input("Press Enter to return to menu...")
        elif choice == '2':
            show_help()
            input("Press Enter to return to menu...")
        elif choice == '3':
            show_hall()
            input("Press Enter to return to menu...")
        elif choice == '4':
            show_credits()
            input("Press Enter to return to menu...")
        elif choice == '5':
            save_hall()
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice.")
            input("Press Enter...")

if __name__ == '__main__':
    main()
