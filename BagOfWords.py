import math

bagOfWordsA = []
bagOfWordsB = []

def openFile(fileName, flag):
    file = open(fileName, 'r')
    textArq = file.readlines()
    storageArray = []
    for text in textArq:
        storageArray.append(text.lower())
    removeStopWords(storageArray, flag)

def removeStopWords(book, flag):
    grammar = ["e","ou","o","a","os","as","ao","aos","do","da","dos","das","no","na","nos","nas","pelo","pela","pelos","pelas","um","uma","uns","umas","dum","duma","duns","dumas","num","numa","nuns","numas", "a","ante","apos","ate","com","conforme","contra","consoante","de","desde","durante","em","excepto","entre","mediante","para","perante","por","salvo","sem","segundo","sob","sobre","tras"]
    string = book[0].split()
    for word in grammar:
        if word in string:
            string.remove(word)
    if flag == 1:
        setInBagOfWordsA(string)
    if flag == 2:
        setInBagOfWordsB(string)

def setInBagOfWordsA(book):
    for text in book:
        if text not in bagOfWordsA:
            bagOfWordsA.append(text)

def setInBagOfWordsB(book):
    for text in book:
        if text not in bagOfWordsB:
            bagOfWordsB.append(text)

def compareDocuments():
    for itemA in bagOfWordsA:
        for itemB in bagOfWordsB:
            if itemA == itemB:
                print(itemA)

openFile("BookA.txt", 1)
openFile("BookB.txt", 2)
compareDocuments()
#print(bagOfWordsA)
#print(bagOfWordsB)