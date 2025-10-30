"""
Display Module
Handles all user interface display functions.
"""

import os


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_welcome():
    """Display welcome message."""
    print("=" * 50)
    print("          WELCOME TO HANGMAN!")
    print("=" * 50)
    print("\nGuess the word letter by letter.")
    print("You have 6 wrong guesses before game over.")
    print("Commands: 'guess' - guess full word, 'quit' - exit game")


def show_game_state(display_word, guessed_letters, remaining_attempts, ascii_art):
    """
    Display the current game state.
    
    Args:
        display_word: Current word progress with underscores
        guessed_letters: Set of guessed letters
        remaining_attempts: Number of remaining attempts
        ascii_art: ASCII art hangman drawing
    """
    print("\n" + "-" * 50)
    print(ascii_art)
    print("-" * 50)
    print(f"\nWord: {display_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Remaining attempts: {remaining_attempts}")
    print("-" * 50)