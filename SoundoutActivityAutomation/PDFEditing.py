#This is a program to automate creating lined a sound out activity I use for teaching
#Louis Faunce - made 06/20/2025
import random

soundOutList = [] #sets up list for words

with open("SoundOutInput.txt", "r") as file: #reads file and puts to list, removing whitespace. "r" is for read only
    for line in file:
        soundOutList.append(line.strip().split("\t")) #formats the words into the list (use * when printing or writing to new file to remove [""]


def randomSpelling():
    for i in range(len(soundOutList)): #loops through each word in the list and randomizes
        soundOutList[i]= ''.join(random.sample(*soundOutList[i],len(*soundOutList[i]))) 


randomSpelling()

levelOneWords = soundOutList[0:4] #first four words, level 1 difficulty, followed by setting up lists for each level
levelTwoWords = soundOutList[5:9] 
levelThreeWords = soundOutList[10:14] 
levelFourWords = soundOutList[15:19] 
levelFiveWords = soundOutList[20:22] 




#function for making words into katakana
def katakanaize():

    return 0 



#format for output to be sent to new file will be "kana ・ jumbled word"

def printTests():
    print("Sound Out Activity Words:", *soundOutList) #prints header
    print("Level 1 Words: ", *levelOneWords) #prints level 1 words
    print("Level 2 Words: ", *levelTwoWords) #prints level 2 words
    print("Level 3 Words: ", *levelThreeWords) #prints level 3 words
    print("Level 4 Words: ", *levelFourWords) #prints level 4 words
    print("Level 5 Words: ", *levelFiveWords) #prints level 5 words