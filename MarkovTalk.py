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
            processLine(line, TM)
            line = f.readline()
            #print(repr(line)) #for debugging

        # move file pointer back to the beginning
        f.seek(0, 0)

def processLine(line, TM):
    """
    
    """
    pass

if __name__ == "__main__":
    main()