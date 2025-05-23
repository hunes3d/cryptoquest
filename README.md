# 🚀 CryptoQuest

CryptoQuest is an interactive, terminal-based cryptography game designed to teach and challenge players with three core puzzles.

---

## 🎯 Objectives

- **Learn cryptographic algorithms:** Caesar Shift, Vigenère Cipher, SHA-256 hashing (with salt)
- **Encourage strategic problem-solving and hint management**
- **Foster friendly competition** via a persistent Hall of Heroes leaderboard
- **Ensure cross-platform compatibility** with a pure ASCII interface

---

## ✨ Features

### 🏠 Main Menu Options
- ▶️ Play
- ℹ️ Help
- 🏆 Hall of Heroes
- 👤 Credits
- 💾 Save & Quit

### 📖 Interactive Tutorial & Help
- `H`: request a hint (score penalty)
- `A`: reveal answer (auto-fail + penalty)
- `?`: display help menu
- `Q`: quit to main menu

### 🧩 Three Puzzle Levels
- **Level 1 – Caesar Shift**: random shift of a keyword
- **Level 2 – Vigenère Cipher**: keyword-based shifting
- **Level 3 – HashLab (SHA-256)**: match hashed keyword + salt

### 💡 Hint System (max 3 hints per run, 2 per level)
- **1st hint:** reveals shift (level 1) or first letter – 50% question points
- **2nd hint:** reveals random letter from secret – 75% question points
- **Reveal:** answer revealed, earn 0 points + –50 overall penalty

### 🏅 Scoring
- Base points per puzzle: **100**
- Hints reduce earned points (50% or 75%)
- Reveal answer: **0** + –50 overall penalty

### 🏆 Hall of Heroes
- Final scores saved in `hall_of_heroes.json`
- Top 3 players awarded medals: 🥇 🥈 🥉

---

## 👥 Credits

- **Author**: Güneş Yılmaz
- **Instructor**: Hicabi Yeniay (AP CSP)

---

## 🛠️ Installation & Usage

```sh
git clone https://github.com/yourusername/cryptoquest.git
cd cryptoquest
python cryptoquest.py
```
- `hall_of_heroes.json` will be auto-generated to store scores.

---

## 📂 Code Structure

- `cryptoquest.py`: main game script
- `hall_of_heroes.json`: persistent high score file

**Key functions:**  
`caesar_cipher()`, `vigenere_cipher()`, `hash_lab()`  
`get_hint()`, `show_help()`, `tutorial()`, `play()`, `main()`

Configuration:  
Easily adjust keywords, shifts, hint limits, and scoring at the top of `cryptoquest.py`.

---

## 🤝 Contributing

Fork the repo, create a feature branch, and submit a pull request.  
Bug reports and enhancements welcome!

---

## 📄 License

MIT License — see [LICENSE](LICENSE) file.

---

Enjoy testing your cryptography skills with CryptoQuest! 🔐🎮
