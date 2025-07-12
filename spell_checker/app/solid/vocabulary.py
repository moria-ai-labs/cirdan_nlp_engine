from abc import ABC, abstractmethod

class Vocabulary(ABC):
    @abstractmethod
    def __contains__(self, word: str) -> bool:
        pass

    @abstractmethod
    def get_words(self) -> set:
        pass

class SimpleVocabulary(Vocabulary):
    def __init__(self, words: set):
        self._words = words

    def __contains__(self, word: str) -> bool:
        return word in self._words

    def get_words(self) -> set:
        return self._words
