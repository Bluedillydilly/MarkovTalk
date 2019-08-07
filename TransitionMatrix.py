from numpy import zeros, sum

class TransitionMatrix:
    """
        A class for the transition matrix involved with markov chain models
    """

    def __init__(self):
        """
            Constructor for a TransitionMatrix.

            Params:
        """
        self.keys = {}
        self.keyCount = 0
        self.matrix = [[]]

    def addKey(self, word):
        """
            A new word to add as a key to the transition matrix.
        """
        if word not in self.keys.keys():
            self.keys[word] = self.getKeyCount()
            self.keyCount += 1

    def getKeyCount(self):
        return self.keyCount

    def get(self, before, after):
        return self.matrix[self.keys[before.lower()]][self.keys[after.lower()]]

    def initMatrix(self):
        for row in range(self.getKeyCount):
            self.matrix[row] = zeros(self.getKeyCount())

    def addToMatrix(self, before, after):
        """
            Adds a WORD - WORD to the matrix.
            Increases the element to show the before is followed by after.

        """
        self.matrix[self.keys[before.lower()]][self.keys[after.lower()]] += 1

    def normalize(self):
        """
            turns the raw counts into ratios that sum to 1 for the row
        """
        for row in range(self.getKeyCount):
            self.matrix[row] /= sum(self.matrix[row])

    def __repr__(self):
        """
            A text representation of transition Matrix.
            WIP, table look?
        """
        print(self.matrix) 