# 🎮 Number Duel Game

A simple two-player number-based strategy game implemented in Python.  
This project was developed for educational purposes to demonstrate class usage, modular structure, and user input handling.

---

## 📋 Game Rules

- Each player receives **6 random numbers** (range: 1–9).
- Players take turns **choosing a sequence** of their numbers to compete in **3 rounds**:
  - **Round 1:** Compare a single selected number. Highest wins.
  - **Round 2:** Compare the **sum of two numbers mod 10**. Highest wins.
  - **Round 3:** Compare the **product of three numbers**. Highest wins.
- The player who wins **2 out of 3 rounds** wins the game.

---

## 🚀 How to Run

### Step 1: Clone the repository
```bash
git clone https://github.com/yzh888/number-duel.git
cd number-duel
```

### Step 2: Run the game
```bash
python main.py
```

---

## 🧠 Example Gameplay
```
Welcome to Number Duel!

Player 1, your numbers are: [3, 8, 6, 1, 5, 9]
Enter the index for your first number (0-5): 1
...

====== Round 1 ======
Player 1: 8
Player 2: 6
Player 1 wins this round!
```

---

## 📁 Project Structure

```
number-duel/
│
├── main.py         # Game launcher
├── player.py       # Player class and number selection
├── game.py         # Round logic and comparison
└── README.md       # This file
```

---

## 🔧 Requirements

- Python 3.x  
- No external libraries needed (uses `random` and `input()`)

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use or modify it for your own educational or personal projects.

