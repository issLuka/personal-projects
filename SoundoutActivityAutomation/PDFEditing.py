#This is a program to automate creating lined a sound out activity I use for teaching
#Louis Faunce - made 06/20/2025
import random

soundOutList = [] #sets up list for words

with open("SoundOutInput.txt", "r") as file: #reads file and puts to list, removing whitespace. "r" is for read only
    for line in file:
        soundOutList.append(line.strip().split("\t")) #formats the words into the list (use * when printing or writing to new file to remove [""]

randomizeList = soundOutList.copy() #sets up list for randomized words

def randomSpelling():
    #randomizeList = soundOutList.copy()
    for i in range(len(randomizeList)): #loops through each word in the list and randomizes
        randomizeList[i]= ''.join(random.sample(*randomizeList[i],len(*randomizeList[i]))) 
    return randomizeList #returns the randomized list

def printTests():
    print("Sound Out Activity Words:", *soundOutList) #prints header
    print("Level 1 Words: ", *levelOneWords) #prints level 1 words
    print("Level 2 Words: ", *levelTwoWords) #prints level 2 words
    print("Level 3 Words: ", *levelThreeWords) #prints level 3 words
    print("Level 4 Words: ", *levelFourWords) #prints level 4 words
    print("Level 5 Words: ", *levelFiveWords) #prints level 5 words

def katakanaize():

    return 0 

randomSpelling()

levelOneWords = randomizeList[0:4] #first four words, level 1 difficulty, followed by setting up lists for each level
levelTwoWords = randomizeList[5:9] 
levelThreeWords = randomizeList[10:14] 
levelFourWords = randomizeList[15:19] 
levelFiveWords = randomizeList[20:22] 

printTests() #prints the lists to the console




#format for output to be sent to new file will be "kana ・ jumbled word"

