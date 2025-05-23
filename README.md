CryptoQuest

CryptoQuest is an interactive, terminal-based cryptography game designed for educational purposes. Players progress through three escalating puzzle levels—Caesar Shift, Vigenère Cipher, and HashLab (SHA‑256 + salt)—while earning points, using hints, and competing for a spot in the Hall of Heroes.

🎯 Objectives

Teach core cryptography concepts: Caesar cipher, Vigenère cipher, and cryptographic hashing with salt.

Encourage problem-solving through timed puzzles, limited hints, and strategic scoring.

Promote healthy competition with persistent high-score tracking (Hall of Heroes).

Ensure accessibility: pure ASCII UI, cross-platform (Windows & Unix), Python 3.

🚀 Features

Main Menu

Play, Help, Hall of Heroes, Credits, Save & Quit options.

Tutorial & Help

Step-by-step tutorial on game rules and scoring.

Help menu with commands (H for hint, A to reveal, ? for help, Q to quit).

Three Puzzle Levels

Level 1: Caesar Shift with a random shift.

Level 2: Vigenère Cipher with random keyword.

Level 3: HashLab: match SHA‑256 hash plus salt.

Hint System

Total of 3 hints per run (max 2 per level).

1st hint: reveal shift (Level 1) or first letter; ★50% score penalty.

2nd hint: random secret letter; ★75% score penalty.

Scoring

Base score: 100 points per puzzle.

Reveal answer: 0 points + –50 points penalty.

Progressive deductions tied to hint usage.

Hall of Heroes

Persistent JSON file stores player names and final scores.

Top 3 players awarded 🥇🥈🥉 medals.

Credits

Author: Güneş Yılmaz

Instructor: Hicabi Yeniay (AP CSP)

🛠️ Installation & Usage

Requirements: Python 3.x, standard library only.

Download cryptoquest.py and hall_of_heroes.json (auto-generated).

Run:

python cryptoquest.py

Enjoy the game and challenge your friends!

🔧 Code Structure

cryptoquest.py: main game code.

Functions:

caesar_cipher / vigenere_cipher / hash_lab: cipher implementations.

get_hint, show_help, tutorial: UI & hint logic.

play(): core loop for puzzles & scoring.

main(): menu navigation.

Configuration at top: easy to adjust keywords, shifts, hint limits, scoring.

🤝 Contribution

Contributions, bug reports, and feature requests are welcome! Please fork the repo and submit a pull request.

Enjoy learning cryptography with CryptoQuest!

