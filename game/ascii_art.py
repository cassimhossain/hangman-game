"""
ASCII Art for Hangman
Contains the hangman drawings for different game states.
"""


HANGMAN_STATES = {
    0: """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    1: """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    2: """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    3: """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    4: """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    5: """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    6: """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
}


def get_hangman_art(wrong_guesses):
    """
    Get the ASCII art for the current game state.
    
    Args:
        wrong_guesses: Number of wrong guesses (0-6)
        
    Returns:
        String containing the ASCII art
    """
    return HANGMAN_STATES.get(wrong_guesses, HANGMAN_STATES[6])