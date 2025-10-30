"""
Hangman Game - Main Entry Point
Author: Your Name
Date: 2025-10-27

This is the main entry point for the Hangman game.
It controls the game flow and coordinates between different modules.
"""

from pathlib import Path
from game.engine import create_game_state, guess_letter, guess_word, get_display_word
from game.engine import is_game_over, has_won, calculate_score, save_log
from game.wordlist import load_wordlist, get_random_word, get_categories
from ui.display import clear_screen, show_welcome, show_game_state
from game.ascii_art import get_hangman_art
import json


def load_statistics():
    """Load game statistics from file."""
    stats_file = Path("game_log/statistics.json")
    if stats_file.exists():
        with open(stats_file, 'r') as f:
            return json.load(f)
    return {
        "games_played": 0,
        "wins": 0,
        "losses": 0,
        "total_score": 0
    }


def save_statistics(stats):
    """Save game statistics to file."""
    stats_file = Path("game_log/statistics.json")
    stats_file.parent.mkdir(parents=True, exist_ok=True)
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=4)


def display_statistics(stats):
    """Display current game statistics."""
    games = stats["games_played"]
    wins = stats["wins"]
    losses = stats["losses"]
    total_score = stats["total_score"]
    
    win_rate = (wins / games * 100) if games > 0 else 0
    avg_score = (total_score / games) if games > 0 else 0
    
    print(f"\n{'='*50}")
    print(f"Games played: {games} | Wins: {wins} | Losses: {losses}")
    print(f"Win rate: {win_rate:.2f}% | Average score: {avg_score:.2f}")
    print(f"Total score: {total_score}")
    print(f"{'='*50}\n")


def get_category_choice(categories):
    """Get category choice from user."""
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    print(f"{len(categories) + 1}. All categories (random)")
    
    while True:
        choice = input("\nEnter category number: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                return categories[idx]
            elif idx == len(categories):
                return None
        print("Invalid choice. Please try again.")


def play_game(wordlist, game_number, stats):
    """Play a single game of Hangman."""
    clear_screen()
    show_welcome()
    
    # Get category choice
    categories = get_categories(wordlist)
    category = get_category_choice(categories)
    
    # Select word
    word, actual_category = get_random_word(wordlist, category)
    
    # Initialize game state
    game_state = create_game_state(word, actual_category, game_number)
    
    # Show initial state
    print(f"\nNew word selected from '{actual_category}' (length {len(word)})")
    show_game_state(
        get_display_word(game_state),
        game_state['guessed_letters'],
        game_state['remaining_attempts'],
        get_hangman_art(game_state['wrong_guesses'])
    )
    
    # Game loop
    while not is_game_over(game_state):
        user_input = input("\nEnter a letter (or type 'guess' to guess full word, 'quit' to exit): ").strip().lower()
        
        if user_input == 'quit':
            print("Thanks for playing!")
            return False
        
        if user_input == 'guess':
            full_guess = input("Enter your guess for the full word: ").strip().lower()
            result = guess_word(game_state, full_guess)
            print(result)
        else:
            result = guess_letter(game_state, user_input)
            print(result)
        
        # Show updated state
        show_game_state(
            get_display_word(game_state),
            game_state['guessed_letters'],
            game_state['remaining_attempts'],
            get_hangman_art(game_state['wrong_guesses'])
        )
    
    # Game over
    if has_won(game_state):
        score = calculate_score(game_state)
        print(f"\n*** You win! Word: {word} ***")
        print(f"Points earned this round: {score}")
        stats["wins"] += 1
        stats["total_score"] += score
    else:
        print(f"\n*** Game over! The word was: {word} ***")
        stats["losses"] += 1
    
    stats["games_played"] += 1
    
    # Save log
    save_log(game_state, stats)
    
    # Display statistics
    display_statistics(stats)
    
    return True


def main():
    """Main game loop."""
    # Initialize paths
    Path("game_log").mkdir(parents=True, exist_ok=True)
    
    # Load wordlist
    wordlist = load_wordlist()
    
    # Load statistics
    stats = load_statistics()
    
    # Game counter
    game_number = stats["games_played"] + 1
    
    # Main game loop
    while True:
        continue_playing = play_game(wordlist, game_number, stats)
        
        if not continue_playing:
            break
        
        # Save statistics
        save_statistics(stats)
        
        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing Hangman!")
            break
        
        game_number += 1
    
    # Final save
    save_statistics(stats)


if __name__ == "__main__":
    main()