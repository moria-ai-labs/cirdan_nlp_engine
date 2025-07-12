import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from spell_checker.app.solid.vocabulary import SimpleVocabulary
from spell_checker.app.solid.levenshtein_distance import LevenshteinDistance
from spell_checker.app.solid.spell_checker import SpellChecker

class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        vocabulary = SimpleVocabulary({"apple", "banana", "cherry", "date"})
        distance_metric = LevenshteinDistance()
        self.spell_checker = SpellChecker(vocabulary, distance_metric)

    def test_word_in_vocabulary(self):
        self.assertTrue(self.spell_checker.word_validation("apple"))

    def test_word_not_in_vocabulary(self):
        self.assertEqual(self.spell_checker.word_validation("aple"), "apple")
        self.assertEqual(self.spell_checker.word_validation("bannana"), "banana")
        self.assertEqual(self.spell_checker.word_validation("grape"), "date")

if __name__ == '__main__':
    unittest.main()
