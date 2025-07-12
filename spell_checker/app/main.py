import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from spell_checker.app.solid.vocabulary import SimpleVocabulary
from spell_checker.app.solid.distance_metric import EditDistance
from spell_checker.app.solid.spell_checker import SpellChecker

def word_validation(word: str):
    vocabulary = SimpleVocabulary({"apple", "banana", "cherry", "date"})
    distance_metric = EditDistance()
    spell_checker_instance = SpellChecker(vocabulary, distance_metric)
    return spell_checker_instance.word_validation(word)


# Example Usage
if __name__ == "__main__":
    # Test cases
    print(word_validation("apple"))
    print(word_validation("aple"))
    print(word_validation("bannana"))
    print(word_validation("grape"))
