import json, random

def readFile(file):
    
    f = open(file)
    data = json.load(f)
    fileData = data['data']
    f.close()
    return fileData

def getRandomWord(words):
    return random.choice(words)


wordList = readFile('words.json')
word = getRandomWord(wordList)
print(word)