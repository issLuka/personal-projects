import random

soundOutList = [] #list to hold the words from the file

with open("SoundOutInput.txt", "r") as file: #reads file and puts to list, removing whitespace. "r" is for read only
    for line in file:
        soundOutList.append(line.strip().split("\t")) #formats the words into the list (use * when printing or writing to new file to remove [""]

randomizeList = soundOutList.copy() #sets up list for randomized words copying og list
soundOutCopy = soundOutList.copy() #copy of original list for spell checking
def randomSpelling(): #self explanatory function to randomize the words in the list

    for i in range(len(randomizeList)):
        randomizeList[i] = ''.join(random.sample(*randomizeList[i],len(*randomizeList[i]))) #randomizes each word in the list

    return randomizeList #returns the randomized list

randomSpelling() #randomizes spelling in list

def spellCheck():
    for i in range(len(randomizeList)):
        check = all(x == y for x, y in zip(soundOutCopy, randomizeList))
        if check == True:
            randomSpelling()
        else:
            break            

spellCheck() #checks the spelling if same as og list

levelOneWords = randomizeList[0:4] #first four randomized words, level 1 difficulty, followed by setting up lists for each level
levelTwoWords = randomizeList[5:9] 
levelThreeWords = randomizeList[10:14] 
levelFourWords = randomizeList[15:19] 
levelFiveWords = randomizeList[20:22] 

def addSpaceToWords(): #will add words to each level
    for i in range(len(levelOneWords)):
        levelOneWords[i] = " ".join(levelOneWords[i])
    for i in range(len(levelTwoWords)):
        levelTwoWords[i] = " ".join(levelTwoWords[i])
    for i in range(len(levelThreeWords)):
        levelThreeWords[i] = " ".join(levelThreeWords[i])
    for i in range(len(levelFourWords)):
        levelFourWords[i] = " ".join(levelFourWords[i])
    for i in range(len(levelFiveWords)):
        levelFiveWords[i] = " ".join(levelFiveWords[i])

#addSpaceToWords()


print("Original List:", *soundOutList)
print("Randomized List:\n", *levelOneWords, "\n", *levelTwoWords, "\n", *levelThreeWords, "\n", *levelFourWords, "\n", *levelFiveWords)