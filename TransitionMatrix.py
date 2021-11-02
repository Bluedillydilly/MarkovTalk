from numpy import zeros, sum
from dataclasses import dataclass
from typing import List, Tuple, TypedDict, NamedTuple, Dict
from functools import reduce

@dataclass
class TransitionMatrix:
    """
        A class for the transition matrix involved successors of words in text.
    """
    words: List[str] = []
    word_count: int = 0
    matrix: Dict[str,Dict[str, float]] = {}

    def initializeMatrix(self) -> None:
        """Initializes a N x N matrix dependent on words list.
        """
        self.matrix = zeros((self.word_count, self.word_count))


    def addWord(self, word: str) -> None:
        """A new word to add as a key to the transition matrix.

            Param:
                word: potential new word to add
        """
        if word.lower() not in self.words:
            # add to word list
            self.words.append( word.lower() )
            self.word_count += 1
            # add to occurrence
            self.matrix[ word ] = []



    def getWords(self) -> List[str]:
        """Gets the list of words in matrix

            Return:
                list of all words in the transition matrix.
        """
        return self.words


    def get(self, before: str, after: str) -> float:
        """
            Get the number of BEFORE - AFTER word pair frequency.
            After normalizing, gets the density of the pair.

            Param:
                before: first word in pair
                after: second word in pair

            Return:
                freqency/density of BEFORE - AFTER occurrence
        """
        return self.matrix[before][after]


    def getRow(self, word) -> Dict[str, float]:
        """
            Gets after words of a before word.

            Return:
                dict of after words to frequency/density
        """
        return self.matrix[word]

    def addPairs(self, pairs: List[(str, str)]) -> None:
        """
            Add multiple BEFORE - AFTER word pairs.

            Param:
                pairs: list of BEFORE - AFTER pair to add
        """
        for (before, after) in pairs:
           self.matrix[before][after] = self.matrix[before].get(after, 0)

    def addPair(self, before, after) -> None:
        """
            Adds a WORD - WORD pair to the matrix.
            Increases the element to show the before is followed by after.

        """
        self.matrix[before][after] = self.matrix[before].get(after, 0)


    def normalize(self) -> None:
        """
            turns the AFTER word frequencies into densities that sum to 1 for the AFTER row. 
        """
        for (before,v) in self.matrix.items():
            # number of total pairs for BEFORE 
            rowCount: int = reduce( sum, v.values() )
            # update counts
            for after in v.keys():
                self.matrix[before][after] /= rowCount
