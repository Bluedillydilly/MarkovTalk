from TransitionMatrix import TransitionMatrix

def main():
    """

    """
    # the transition matrix involved with mapping the words
    TM = TransitionMatrix()
    
    inputText = str(input("Name of input text file: "))

    with open(inputText, "r") as f:
        line = f.readline()
        while line:
            addKeys(line, TM)
            line = f.readline()

        print(TM)
        TM.initMatrix()
        print(TM)
        # move file pointer back to the beginning
        f.seek(0, 0)
        line = f.readline()
        while line:
            addEntries(line, TM)
            line = f.readline()
    print(TM)
    TM.normalize()
    print(TM)

def processLine(line):
    """
    
    """
    punc = [',', '.', '?', '!']
    line = line.split()
    lineSplit = []
    for word in line:
        if word[-1] in punc:
            lineSplit.append(word[:-1].lower())
            lineSplit.append(word[-1].lower())
        else:
            lineSplit.append(word.lower())
    return lineSplit
    
    
def addKeys(line, TM):
    lineProcessed = processLine(line)
    for word in lineProcessed:
        TM.addKey(word)

def addEntries(line, TM):
    wordAdj = processLine(line)
    for i in range(len(wordAdj)-1):
        TM.addToMatrix(wordAdj[i], wordAdj[i+1])

if __name__ == "__main__":
    main()