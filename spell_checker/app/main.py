import sys
import os
import argparse

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from spell_checker.app.solid.vocabulary import SimpleVocabulary
from spell_checker.app.solid.levenshtein_distance import LevenshteinDistance
from spell_checker.app.solid.distance_metric import EditDistance
from spell_checker.app.solid.spell_checker import SpellChecker

def word_validation(word: str, metric: str = "levenshtein"):
    vocabulary = SimpleVocabulary({"apple", "banana", "cherry", "date"})

    if metric == "levenshtein":
        distance_metric = LevenshteinDistance()
    elif metric == "editdistance":
        distance_metric = EditDistance()
    else:
        raise ValueError("Invalid distance metric specified.")

    spell_checker_instance = SpellChecker(vocabulary, distance_metric)
    return spell_checker_instance.word_validation(word)


# Example Usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spell Checker")
    parser.add_argument("word", type=str, help="The word to validate.")
    parser.add_argument("--metric", type=str, default="levenshtein", choices=["levenshtein", "editdistance"],
                        help="The distance metric to use.")
    args = parser.parse_args()

    result = word_validation(args.word, args.metric)
    print(result)
