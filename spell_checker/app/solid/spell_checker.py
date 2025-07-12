from .vocabulary import Vocabulary
from .distance_metric import DistanceMetric

class SpellChecker:
    def __init__(self, vocabulary: Vocabulary, distance_metric: DistanceMetric):
        self.vocabulary = vocabulary
        self.distance_metric = distance_metric

    def word_validation(self, word: str):
        if word in self.vocabulary:
            return True

        words = self.vocabulary.get_words()
        closest_word = min(words, key=lambda x: self.distance_metric.calculate(word, x))
        return closest_word
