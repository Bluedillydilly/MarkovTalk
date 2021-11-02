from numpy import zeros, sum
from dataclasses import dataclass
from typing import List, Tuple, TypedDict, NamedTuple, Dict

@dataclass
class TransitionMatrix:
    """
        A class for the transition matrix involved successors of words in text.
    """
    words: List[str] = []
    word_count: int = 0
    matrix: Dict[str,Dict[str, float]] = {}

    def initializeMatrix(self) -> None:
        """
            Initializes a N x N matrix dependent on words list.
        """
        self.matrix = zeros((self.word_count, self.word_count))


    def addWord(self, word: str) -> None:
        """
            A new word to add as a key to the transition matrix.
        """
        if word.lower() not in self.words:
            # add to word list
            self.words.append( word.lower() )
            self.word_count += 1
            # add to occurrence
            self.matrix[ word ] = []



    def getWords(self) -> List[str]:
        """
            Gets the list of words in matrix
        """
        return self.words


    def get(self, before: str, after: str) -> float:
        """
            Get the number of BEFORE - AFTER word pair frequency.
            After normalizing, gets the density of the pair.
        """
        return self.matrix[before][after]


    def getRow(self, word) -> Dict[str, float]:
        """
            Gets after words of a before word.
        """
        return self.matrix[word]

    def addPairs(self, pairs: List[(str, str)]) -> None:
        """
            Add multiple BEFORE - AFTER word pairs.
        """
        for (before, after) in pairs:
            pass

    def addPair(self, before, after):
        """
            Adds a WORD - WORD pair to the matrix.
            Increases the element to show the before is followed by after.

        """
        self.matrix[self.keys[before]][self.keys[after]] += 1


    def normalize(self):
        """
            turns the raw counts into ratios that sum to 1 for the row
        """
        for row in range(self.getKeyCount()):
            self.matrix[row] /= sum(self.matrix[row])
