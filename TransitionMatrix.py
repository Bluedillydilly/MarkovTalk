from numpy import zeros, sum, random
from dataclasses import dataclass, field
from typing import List, Set, Tuple, TypeVar, TypedDict, NamedTuple, Dict, Generic
from functools import reduce

T = TypeVar("T")

class Pair(NamedTuple):
    before: str
    after: str

@dataclass
class TransitionMatrix(Generic[T]):
    """
        A class for the transition matrix involved successors of words in text.
    """
    words: Set[T] = field(default_factory=set)
    word_count: int = 0
    matrix: Dict[T,Dict[T, float]] = field(default_factory=dict)

    def initializeMatrix(self) -> None:
        """Initializes a N x N matrix dependent on words list.
        """
        self.matrix = zeros((self.word_count, self.word_count))


    def addWord(self, word: T) -> None:
        """A new word to add as a key to the transition matrix.

            Param:
                word: potential new word to add
        """
        if word not in self.words:
            # add to word list
            self.words.add( word )
            self.word_count += 1
            # add to occurrence
            self.matrix[ word ] = {}



    def getWords(self) -> set:
        """Gets the list of words in matrix

            Return:
                list of all words in the transition matrix.
        """
        return self.words


    def get(self, before: T, after: T) -> float:
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

    def getRow(self, before: T ) -> List[float]:
        """
            
        """
        return self.matrix[before]

    def getNext(self, before: T ) -> T:
        """
            Gets the after word given the before word.
        """
        return random.choice( list(self.matrix[before].keys()), p=list(self.matrix[before].values()) )

    def addPairs(self, pairs: List[Pair]) -> None:
        """
            Add multiple BEFORE - AFTER word pairs.

            Param:
                pairs: list of BEFORE - AFTER pair to add
        """
        for (before, after) in pairs:
           self.addPair( before, after)

    def addPair(self, before, after) -> None:
        """
            Adds a WORD - WORD pair to the matrix.
            Increases the element to show the before is followed by after.

        """
        self.addWord( before )
        self.addWord( after )
        self.matrix[before][after] = self.matrix[before].get(after, 0) + 1


    def normalize(self) -> None:
        """
            turns the AFTER word frequencies into densities that sum to 1 for the AFTER row. 
        """
        for (before, afterDict) in self.matrix.items():
            if not len(afterDict.values()):
                continue
            # number of total pairs for BEFORE 
            rowCount: int = reduce( lambda x, y: x+y, afterDict.values() )
            # update counts
            for after in afterDict.keys():
                self.matrix[before][after] /= rowCount

if __name__ == "__main__":
    print(__file__)

    tm: TransitionMatrix = TransitionMatrix()

    pairs: List[Pair] = [  
        (__file__[ i ], __file__[ i+1 ]) for i in range(len(__file__) -1) ]
    print(f"Init word pairs: {pairs}")
        
    tm.addPairs( pairs )

    tm.normalize()

    print( tm.getNext('i'))

    

