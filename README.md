Hangman Game
A terminal-based Hangman game with categories, scoring, and persistent statistics.

Features
Multiple categories: Animals, Countries, Programming, Science
Scoring system with penalties for wrong guesses
Persistent statistics tracking across sessions
ASCII art hangman that updates with each wrong guess
Detailed game logs for each session
Input validation and error handling
Full word guessing option
Project Structure
hangman_game/
├── main.py                 # Entry point
├── words/
│   ├── words.txt          # Main word list (optional)
│   └── categories/        # Category-specific word files (optional)
│       ├── animals.txt
│       ├── countries.txt
│       ├── programming.txt
│       └── science.txt
├── game/
│   ├── engine.py          # Core game logic
│   ├── wordlist.py        # Word loading and selection
│   └── ascii_art.py       # Hangman ASCII art
├── ui/
│   └── display.py         # Display functions
├── game_log/
│   ├── statistics.json    # Persistent statistics
│   └── game1/            # Individual game logs
│       └── log.txt
└── README.md
How to Run
Ensure you have Python 3.7+ installed
Navigate to the hangman_game directory
Run the game:
bash
   python main.py
Wordlist Format
Option 1: Single File
Place all words in words/words.txt, one word per line:

elephant
giraffe
python
Option 2: Category Files
Create separate files in words/categories/:

animals.txt
countries.txt
programming.txt
science.txt
Each file should contain words for that category, one per line.

Default Words
If no word files are found, the game uses built-in default categories with sample words.

Scoring Method
The scoring system rewards longer words and penalizes wrong guesses:

Formula: (word_length × 10) - (wrong_guesses × 5)

Examples:

Word: "python" (6 letters), 1 wrong guess: (6 × 10) - (1 × 5) = 55 points
Word: "elephant" (8 letters), 2 wrong guesses: (8 × 10) - (2 × 5) = 70 points
Word: "cat" (3 letters), 0 wrong guesses: (3 × 10) - (0 × 5) = 30 points
Minimum score: 0 (losing gives 0 points)

Game Logs
Each game creates a new folder in game_log/:

game_log/game1/log.txt
game_log/game2/log.txt
etc.
Each log contains:

Selected category and word
Complete guess history (in order)
Wrong guesses list and count
Final result (Win/Loss)
Points earned
Running statistics
Timestamp
Progress trace showing word revelation
Statistics Tracking
The game tracks the following across all sessions:

Games Played: Total number of games
Wins: Number of games won
Losses: Number of games lost
Total Score: Cumulative score across all games
Win Rate: Percentage of games won
Average Score: Average score per game
Statistics are saved in game_log/statistics.json and persist between sessions.

Gameplay
Choose a category or select random
Guess letters one at a time
Type 'guess' to attempt the full word
Type 'quit' to exit
Win by revealing all letters or guessing the full word correctly
Lose after 6 wrong guesses
Commands
Single letter: Guess a letter (e.g., 'a', 'b', 'c')
'guess': Attempt to guess the full word
'quit': Exit the game
Requirements
Python 3.7+
No external dependencies (uses only standard library)
Implementation Details
Modular Design
main.py: Entry point and game flow control
game/engine.py: Core gameplay logic, validation, scoring (function-based)
game/wordlist.py: Word loading and random selection (function-based)
game/ascii_art.py: ASCII art hangman drawings
ui/display.py: All display and formatting functions
All modules use functions only - no classes are used in this implementation.

Path Management
All file operations use pathlib for cross-platform compatibility.

Directory Creation
Folders are created dynamically using mkdir(parents=True, exist_ok=True) to prevent errors.

Game State Management
Game state is managed using dictionaries passed between functions, following functional programming principles.

Author
Created as part of Assignment 1 for Hangman Game project.

License
Educational project - free to use and modify.

