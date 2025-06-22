import random

soundOutList = [] #list to hold the words from the file

with open("SoundOutInput.txt", "r") as file: #reads file and puts to list, removing whitespace. "r" is for read only
    for line in file:
        soundOutList.append(line.strip().split("\t")) #formats the words into the list (use * when printing or writing to new file to remove [""]

randomizeList = soundOutList.copy() #sets up list for randomized words copying og list

def randomSpelling(): #self explanatory function to randomize the words in the list

    for i in range(len(randomizeList)): #loops through each word in the list and randomizes
        randomizeList[i] = ''.join(random.sample(*randomizeList[i],len(*randomizeList[i])))

    return randomizeList #returns the randomized list

randomSpelling()

levelOneWords = randomizeList[0:4] #first four randomized words, level 1 difficulty, followed by setting up lists for each level
levelTwoWords = randomizeList[5:9] 
levelThreeWords = randomizeList[10:14] 
levelFourWords = randomizeList[15:19] 
levelFiveWords = randomizeList[20:22] 

def randomSpellCheck():
    spellCheckBool = False 
    while spellCheckBool == False: #loops through each word in the list
        if levelOneWords[0:4] == soundOutList[0:4]: 
          randomizeList[0:4] = ''.join(random.sample(*randomizeList[0:4],len(*randomizeList[0:4])))
        elif levelTwoWords[5:9] == soundOutList[5:9]: 
            randomizeList[5:9] = ''.join(random.sample(*randomizeList[5:9],len(*randomizeList[5:9])))
        elif levelThreeWords[10:14] == soundOutList[10:14]: 
            randomizeList[10:14] = ''.join(random.sample(*randomizeList[10:14],len(*randomizeList[10:14])))
        elif levelFourWords[15:19] == soundOutList[15:19]: 
            randomizeList[15:19] = ''.join(random.sample(*randomizeList[15:19],len(*randomizeList[15:19])))
        elif levelFiveWords[20:22] == soundOutList[20:22]: 
            randomizeList[20:22] = ''.join(random.sample(*randomizeList[20:22],len(*randomizeList[20:22])))
        else:
            spellCheckBool = True

randomSpellCheck()

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

addSpaceToWords()

levelOneWordOne = " ".join(levelOneWords[0])  # Joins the first word of level one with spaces
levelTwoWordOne = " ".join(levelTwoWords[0])  # Joins the first word of level two with spaces
levelThreeWordOne = " ".join(levelThreeWords[0])  # Joins the first word of level three with spaces
levelFourWordOne = " ".join(levelFourWords[0])  # Joins the first word of level four with spaces
levelFiveWordOne = " ".join(levelFiveWords[0])  # Joins the first word of level five with spaces


print("Original List:", *soundOutList)
print("Randomized List:", *levelOneWords, "\n", *levelTwoWords, "\n", *levelThreeWords, "\n", *levelFourWords, "\n", *levelFiveWords)