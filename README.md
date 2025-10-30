# 🎯 Hangman Game

A terminal-based Hangman game with categories, scoring, and persistent statistics.

---

## 🧩 Features
- Multiple categories: **Animals, Countries, Programming, Science**
- Scoring system with penalties for wrong guesses  
- Persistent statistics tracking across sessions  
- ASCII art hangman that updates with each wrong guess  
- Detailed game logs for each session  
- Input validation and error handling  
- Full word guessing option  

---

## 📁 Project Structure
```

hangman_game/
├── main.py                 # Entry point
├── words/
│   ├── words.txt           # Main word list (optional)
│   └── categories/         # Category-specific word files (optional)
│       ├── animals.txt
│       ├── countries.txt
│       ├── programming.txt
│       └── science.txt
├── game/
│   ├── engine.py           # Core game logic
│   ├── wordlist.py         # Word loading and selection
│   └── ascii_art.py        # Hangman ASCII art
├── ui/
│   └── display.py          # Display functions
├── game_log/
│   ├── statistics.json     # Persistent statistics
│   └── game1/              # Individual game logs
│       └── log.txt
└── README.md
````

## ▶️ How to Run

````
1. Ensure you have **Python 3.7+** installed.  
2. Navigate to the `hangman_game` directory.  
3. Run the game:
   ```bash
   python main.py
````

---

## 📝 Wordlist Format

### Option 1: Single File

Place all words in `words/words.txt`, one word per line:

```
elephant
giraffe
python
```

### Option 2: Category Files

Create separate files in `words/categories/`:

```
animals.txt
countries.txt
programming.txt
science.txt
```

Each file should contain words for that category, one per line.

---

## 🧠 Default Words

If no word files are found, the game uses built-in default categories with sample words.

---

## 💯 Scoring Method

The scoring system rewards longer words and penalizes wrong guesses.

**Formula:**

```
(word_length × 10) - (wrong_guesses × 5)
```

### Examples:

| Word     | Wrong Guesses | Score Calculation  | Points |
| -------- | ------------- | ------------------ | ------ |
| python   | 1             | (6 × 10) - (1 × 5) | 55     |
| elephant | 2             | (8 × 10) - (2 × 5) | 70     |
| cat      | 0             | (3 × 10) - (0 × 5) | 30     |

Minimum score: **0** (losing gives 0 points)

---

## 📂 Game Logs

Each game creates a new folder in `game_log/`:

```
game_log/game1/log.txt
game_log/game2/log.txt
```

Each log contains:

* Selected category and word
* Complete guess history (in order)
* Wrong guesses list and count
* Final result (Win/Loss)
* Points earned
* Running statistics
* Timestamp
* Word revelation trace

---

## 📊 Statistics Tracking

The game tracks the following across all sessions:

| Metric            | Description             |
| ----------------- | ----------------------- |
| **Games Played**  | Total number of games   |
| **Wins**          | Number of games won     |
| **Losses**        | Number of games lost    |
| **Total Score**   | Cumulative score        |
| **Win Rate**      | Percentage of games won |
| **Average Score** | Average score per game  |

Statistics are saved in `game_log/statistics.json` and persist between sessions.

---

## 🎮 Gameplay

1. Choose a category or select **random**
2. Guess letters one at a time
3. Type **guess** to attempt the full word
4. Type **quit** to exit

**Win:** Reveal all letters or guess the full word
**Lose:** 6 wrong guesses

---

## ⌨️ Commands

| Command                        | Action                         |
| ------------------------------ | ------------------------------ |
| Single letter (e.g., `a`, `b`) | Guess a letter                 |
| `guess`                        | Attempt to guess the full word |
| `quit`                         | Exit the game                  |

---

## ⚙️ Requirements

* Python **3.7+**
* No external dependencies (uses only the standard library)

---

## 🧩 Implementation Details

### Modular Design

| File                | Description                              |
| ------------------- | ---------------------------------------- |
| `main.py`           | Entry point and game flow control        |
| `game/engine.py`    | Core gameplay logic, validation, scoring |
| `game/wordlist.py`  | Word loading and random selection        |
| `game/ascii_art.py` | ASCII art hangman drawings               |
| `ui/display.py`     | Display and formatting functions         |

All modules use **functions only** — no classes are used.

---

### Path Management

Uses **pathlib** for cross-platform file handling.

### Directory Creation

Uses:

```python
mkdir(parents=True, exist_ok=True)
```

to safely create folders without errors.

### Game State Management

Game state is stored in dictionaries passed between functions, following **functional programming principles**.

---

## 👤 Author

Created by **Qasim** as part of *Assignment 1 — Hangman Game Project.*

---

## 📜 License

Educational project — free to use and modify.


