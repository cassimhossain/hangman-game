"""
Hangman Game Engine
Contains core gameplay logic including guessing, validation, and scoring.
"""

from pathlib import Path
from datetime import datetime


MAX_WRONG_GUESSES = 6
BASE_SCORE = 10
WRONG_GUESS_PENALTY = 5


def create_game_state(word, category, game_number):
    """
    Create initial game state.
    
    Args:
        word: The word to guess
        category: The category of the word
        game_number: The current game number
        
    Returns:
        Dictionary containing game state
    """
    return {
        'word': word.lower(),
        'category': category,
        'game_number': game_number,
        'guessed_letters': set(),
        'correct_letters': set(),
        'wrong_letters': set(),
        'wrong_guesses': 0,
        'remaining_attempts': MAX_WRONG_GUESSES,
        'guess_history': []  # List of (guess, result) tuples
    }


def guess_letter(game_state, letter):
    """
    Process a letter guess (can be single or multiple letters).
    
    Args:
        game_state: Dictionary containing current game state
        letter: The letter(s) to guess
        
    Returns:
        String message describing the result
    """
    # Validate input
    if not letter:
        return "[X] Please enter at least one letter."
    
    if not letter.isalpha():
        return "[X] Please enter only alphabetic characters."
    
    letter = letter.lower()
    
    # Process multiple letters
    if len(letter) > 1:
        results = []
        for char in letter:
            if char in game_state['guessed_letters']:
                results.append(f"[i] '{char}' already guessed")
            elif char in game_state['word']:
                game_state['guessed_letters'].add(char)
                game_state['correct_letters'].add(char)
                game_state['guess_history'].append((char, "Correct"))
                results.append(f"[+] '{char}' is correct")
            else:
                game_state['guessed_letters'].add(char)
                game_state['wrong_letters'].add(char)
                game_state['wrong_guesses'] += 1
                game_state['remaining_attempts'] -= 1
                game_state['guess_history'].append((char, "Wrong"))
                results.append(f"[-] '{char}' is wrong")
        return "\n".join(results)
    
    # Process single letter
    if letter in game_state['guessed_letters']:
        return f"[i] You already guessed '{letter}'. Try a different letter."
    
    # Add to guessed letters
    game_state['guessed_letters'].add(letter)
    
    # Check if correct
    if letter in game_state['word']:
        game_state['correct_letters'].add(letter)
        game_state['guess_history'].append((letter, "Correct"))
        return f"[+] Correct! The letter '{letter}' is in the word."
    else:
        game_state['wrong_letters'].add(letter)
        game_state['wrong_guesses'] += 1
        game_state['remaining_attempts'] -= 1
        game_state['guess_history'].append((letter, "Wrong"))
        return f"[-] Wrong! The letter '{letter}' is not in the word."


def guess_word(game_state, word_guess):
    """
    Process a full word guess.
    
    Args:
        game_state: Dictionary containing current game state
        word_guess: The full word guess
        
    Returns:
        String message describing the result
    """
    word_guess = word_guess.lower()
    
    if word_guess == game_state['word']:
        # Mark all letters as guessed correctly
        for letter in game_state['word']:
            game_state['correct_letters'].add(letter)
            game_state['guessed_letters'].add(letter)
        game_state['guess_history'].append((f"WORD: {word_guess}", "Correct"))
        return f"[+] Correct! You guessed the word: {game_state['word']}"
    else:
        game_state['wrong_guesses'] += 1
        game_state['remaining_attempts'] -= 1
        game_state['guess_history'].append((f"WORD: {word_guess}", "Wrong"))
        return f"[-] Wrong! '{word_guess}' is not the correct word."


def get_display_word(game_state):
    """
    Get the current display state of the word.
    
    Args:
        game_state: Dictionary containing current game state
        
    Returns:
        String with guessed letters revealed and others as underscores
    """
    return ' '.join([letter if letter in game_state['correct_letters'] else '_' 
                    for letter in game_state['word']])


def is_game_over(game_state):
    """
    Check if the game is over.
    
    Args:
        game_state: Dictionary containing current game state
        
    Returns:
        Boolean indicating if game is over
    """
    return has_won(game_state) or has_lost(game_state)


def has_won(game_state):
    """
    Check if the player has won.
    
    Args:
        game_state: Dictionary containing current game state
        
    Returns:
        Boolean indicating if player won
    """
    return all(letter in game_state['correct_letters'] for letter in game_state['word'])


def has_lost(game_state):
    """
    Check if the player has lost.
    
    Args:
        game_state: Dictionary containing current game state
        
    Returns:
        Boolean indicating if player lost
    """
    return game_state['wrong_guesses'] >= MAX_WRONG_GUESSES


def calculate_score(game_state):
    """
    Calculate the score for a won game.
    
    Formula: (word_length * BASE_SCORE) - (wrong_guesses * WRONG_GUESS_PENALTY)
    
    Args:
        game_state: Dictionary containing current game state
        
    Returns:
        Score (integer), minimum 0
    """
    if not has_won(game_state):
        return 0
    
    base_points = len(game_state['word']) * BASE_SCORE
    penalty = game_state['wrong_guesses'] * WRONG_GUESS_PENALTY
    score = max(0, base_points - penalty)
    return score


def save_log(game_state, stats):
    """
    Save the game log to a file.
    
    Args:
        game_state: Dictionary containing current game state
        stats: Dictionary containing game statistics
    """
    # Create game folder
    game_folder = Path(f"game_log/game{game_state['game_number']}")
    game_folder.mkdir(parents=True, exist_ok=True)
    
    # Create log file
    log_file = game_folder / "log.txt"
    
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f"Game {game_state['game_number']} Log\n")
        f.write(f"{'='*50}\n\n")
        f.write(f"Category: {game_state['category']}\n")
        f.write(f"Word: {game_state['word']}\n")
        f.write(f"Word Length: {len(game_state['word'])}\n\n")
        
        f.write("Guesses (in order):\n")
        for i, (guess, result) in enumerate(game_state['guess_history'], 1):
            f.write(f"{i}. {guess} → {result}\n")
        
        f.write(f"\nWrong Guesses List: {', '.join(sorted(game_state['wrong_letters'])) if game_state['wrong_letters'] else 'None'}\n")
        f.write(f"Wrong Guesses Count: {game_state['wrong_guesses']}\n")
        f.write(f"Remaining Attempts at End: {game_state['remaining_attempts']}\n\n")
        
        result = "Win" if has_won(game_state) else "Loss"
        f.write(f"Result: {result}\n")
        f.write(f"Points Earned: {calculate_score(game_state)}\n\n")
        
        f.write(f"Total Score (after this round): {stats['total_score']}\n")
        f.write(f"Games Played: {stats['games_played']}\n")
        f.write(f"Wins: {stats['wins']}\n")
        f.write(f"Losses: {stats['losses']}\n")
        
        win_rate = (stats['wins'] / stats['games_played'] * 100) if stats['games_played'] > 0 else 0
        f.write(f"Win Rate: {win_rate:.2f}%\n\n")
        
        f.write(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*50}\n\n")
        
        # Session notes
        f.write("Session Notes:\n")
        f.write(f"- ASCII hangman reached state {game_state['wrong_guesses']} after {game_state['wrong_guesses']} wrong guess(es).\n")
        f.write("- Progress trace:\n")
        
        # Reconstruct progress
        progress_states = ["  " + ' '.join(['_'] * len(game_state['word']))]
        temp_correct = set()
        
        for guess, result in game_state['guess_history']:
            if result == "Correct" and not guess.startswith("WORD:"):
                temp_correct.add(guess)
                state = "  -> " + ' '.join([letter if letter in temp_correct else '_' 
                                           for letter in game_state['word']])
                progress_states.append(state)
            elif result == "Wrong":
                state = "  -> " + ' '.join([letter if letter in temp_correct else '_' 
                                           for letter in game_state['word']])
                if guess.startswith("WORD:"):
                    state += f" ({guess} wrong — no progress change)"
                else:
                    state += f" ({guess} wrong — no progress change)"
                progress_states.append(state)
        
        f.write('\n'.join(progress_states))
        f.write(f"\n{'='*50}\n")