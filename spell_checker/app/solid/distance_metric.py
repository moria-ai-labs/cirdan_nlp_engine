from abc import ABC, abstractmethod

class DistanceMetric(ABC):
    @abstractmethod
    def calculate(self, word1: str, word2: str) -> int:
        pass

class EditDistance(DistanceMetric):
    def calculate(self, word1: str, word2: str) -> int:
        import editdistance
        return editdistance.eval(word1, word2)
