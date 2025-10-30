"""
Word List Manager
Handles loading words from files and random selection.
"""

import random
from pathlib import Path


def load_wordlist():
    """
    Load words from files.
    
    Returns:
        Dictionary with categories as keys and word lists as values
    """
    categories = {}
    words_dir = Path("words")
    categories_dir = words_dir / "categories"
    
    # Load from main words.txt if it exists
    main_words_file = words_dir / "words.txt"
    if main_words_file.exists():
        with open(main_words_file, 'r') as f:
            words = [line.strip().lower() for line in f if line.strip()]
            categories['All'] = words
    
    # Load from category files
    if categories_dir.exists():
        for category_file in categories_dir.glob("*.txt"):
            category_name = category_file.stem.capitalize()
            with open(category_file, 'r') as f:
                words = [line.strip().lower() for line in f if line.strip()]
                categories[category_name] = words
    
    # If no words loaded, create default categories with sample words
    if not categories:
        categories = create_default_categories()
    
    return categories


def create_default_categories():
    """
    Create default categories with sample words.
    
    Returns:
        Dictionary with default categories and words
    """
    return {
        'Animals': [
            'elephant', 'giraffe', 'hippopotamus', 'rhinoceros', 'chimpanzee',
            'kangaroo', 'crocodile', 'penguin', 'dolphin', 'octopus',
            'butterfly', 'cheetah', 'leopard', 'gorilla', 'zebra'
        ],
        'Countries': [
            'afghanistan', 'bangladesh', 'cambodia', 'denmark', 'ethiopia',
            'france', 'germany', 'hungary', 'indonesia', 'japan',
            'kazakhstan', 'luxembourg', 'madagascar', 'netherlands', 'pakistan'
        ],
        'Programming': [
            'python', 'javascript', 'algorithm', 'database', 'function',
            'variable', 'compiler', 'debugging', 'framework', 'interface',
            'software', 'hardware', 'network', 'protocol', 'encryption'
        ],
        'Science': [
            'astronomy', 'biology', 'chemistry', 'physics', 'geology',
            'botany', 'zoology', 'ecology', 'genetics', 'evolution',
            'molecule', 'electron', 'neutron', 'proton', 'quantum'
        ]
    }


def get_categories(wordlist):
    """
    Get list of available categories.
    
    Args:
        wordlist: Dictionary of categories and words
        
    Returns:
        List of category names
    """
    return list(wordlist.keys())


def get_random_word(wordlist, category=None):
    """
    Get a random word from the specified category.
    
    Args:
        wordlist: Dictionary of categories and words
        category: Category name, or None for random from all categories
        
    Returns:
        Tuple of (word, actual_category)
    """
    if category and category in wordlist:
        word = random.choice(wordlist[category])
        return word, category
    else:
        # Choose random category
        category = random.choice(list(wordlist.keys()))
        word = random.choice(wordlist[category])
        return word, category


def get_word_count(wordlist):
    """
    Get total number of words across all categories.
    
    Args:
        wordlist: Dictionary of categories and words
        
    Returns:
        Integer count of total words
    """
    return sum(len(words) for words in wordlist.values())