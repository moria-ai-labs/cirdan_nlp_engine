import unittest
from spell_checker.app.solid.vocabulary import SimpleVocabulary
from spell_checker.app.solid.distance_metric import EditDistance
from spell_checker.app.solid.spell_checker import SpellChecker

class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        vocabulary = SimpleVocabulary({"apple", "banana", "cherry", "date"})
        distance_metric = EditDistance()
        self.spell_checker = SpellChecker(vocabulary, distance_metric)

    def test_word_in_vocabulary(self):
        self.assertTrue(self.spell_checker.word_validation("apple"))

    def test_word_not_in_vocabulary(self):
        self.assertEqual(self.spell_checker.word_validation("aple"), "apple")
        self.assertEqual(self.spell_checker.word_validation("bannana"), "banana")
        self.assertEqual(self.spell_checker.word_validation("grape"), "date")

if __name__ == '__main__':
    unittest.main()
