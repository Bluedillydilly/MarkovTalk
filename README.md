# MarkovTalk
Using the principle of markov chains in the form of a matrix (transition matrix) to generate text based on another input text.


## The How

Program is composed of 4 parts
* Markovtalk -  a wrapper for genTM and genText
* genTM - responsible for talking the input text and constructing the transition matrix 
* genText - responsible for generating a potential abitrary amount of new lines of text using the previously generated transition matrix(TM)

## The Goal

## The Future
* Provide an url to extract text from. Support only certain websites? ie wikipedia
* Fix capitialization of words following '.'s, '!'s, and '?'.