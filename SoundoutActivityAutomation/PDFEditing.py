#This is a program to automate creating lined a sound out activity I use for teaching
#Louis Faunce - made 06/20/2025
import random
from e2k import P2K #importing e2k phoneme to kana converter
from g2p_en import G2p #gets g2p library

#------------------------------------------------------------------------------
#section for basic variables
p2k = P2K() #initializing the phoneme to kana converter
g2p = G2p() #initializing the g2p converter
pronunciationList = [] #sets up list for pronunciations
soundOutList = [] #sets up list for words
#------------------------------------------------------------------------------


with open("SoundOutInput.txt", "r") as file: #reads file and puts to list, removing whitespace. "r" is for read only
    for line in file:
        soundOutList.append(line.strip().split("\t")) #formats the words into the list (use * when printing or writing to new file to remove [""]

randomizeList = soundOutList.copy() #sets up list for randomized words copying og list

#------------------------------------------------------------------------------
def randomSpelling(): #self explanatory function to randomize the words in the list

    for i in range(len(randomizeList)): #loops through each word in the list and randomizes
        randomizeList[i] = ''.join(random.sample(*randomizeList[i],len(*randomizeList[i])))

    return randomizeList #returns the randomized list

def katakanaize(): #turn og list to kana

    for i in range(len(soundOutList)): #loops through each word in the list
        katakana = p2k(g2p(*soundOutList[i]))
        #print(katakana) #prints the kana to console for testing
        pronunciationList.append(katakana)
        
    return pronunciationList #returns the kana list

def printTests(): #tests to make sure lists work
    
    print("Sound Out Activity Words:", *soundOutList) #prints header
    print("Level 1 Words: ", *levelOneWords, *levelOneKana) #prints level 1 words
    print("Level 2 Words: ", *levelTwoWords, *levelTwoKana) #prints level 2 words
    print("Level 3 Words: ", *levelThreeWords, *levelThreeKana) #prints level 3 words
    print("Level 4 Words: ", *levelFourWords, *levelFourKana) #prints level 4 words
    print("Level 5 Words: ", *levelFiveWords, *levelFiveKana) #prints level 5 words
    
def addSpaceToWords(): #will add spaces to words in each level
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

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
katakanaize()
randomSpelling()
#------------------------------------------------------------------------------

#grouping of the words into levels based on the difficulty
#------------------------------------------------------------------------------
levelOneWords = randomizeList[0:4] #first four randomized words, level 1 difficulty, followed by setting up lists for each level
levelTwoWords = randomizeList[5:9] 
levelThreeWords = randomizeList[10:14] 
levelFourWords = randomizeList[15:19] 
levelFiveWords = randomizeList[20:22] 

levelOneKana = pronunciationList[0:4] #first four kana, level 1 difficulty, followed by setting up lists for each level
levelTwoKana = pronunciationList[5:9]
levelThreeKana = pronunciationList[10:14]
levelFourKana = pronunciationList[15:19]
levelFiveKana = pronunciationList[20:22]
#------------------------------------------------------------------------------
#def randomSpellCheck():
    #spellCheckBool = False 
    #while spellCheckBool == False: #loops through each word in the list
       # if levelOneWords[0:4] == soundOutList[0:4]: 
          #  randomizeList[0:4] = ''.join(random.sample(*randomizeList[0:4],len(*randomizeList[0:4])))
        #elif levelTwoWords[5:9] == soundOutList[5:9]: 
       #     randomizeList[5:9] = ''.join(random.sample(*randomizeList[5:9],len(*randomizeList[5:9])))
       # elif levelThreeWords[10:14] == soundOutList[10:14]: 
           # randomizeList[10:14] = ''.join(random.sample(*randomizeList[10:14],len(*randomizeList[10:14])))
        #elif levelFourWords[15:19] == soundOutList[15:19]: 
            #randomizeList[15:19] = ''.join(random.sample(*randomizeList[15:19],len(*randomizeList[15:19])))
        #elif levelFiveWords[20:22] == soundOutList[20:22]: 
           # randomizeList[20:22] = ''.join(random.sample(*randomizeList[20:22],len(*randomizeList[20:22])))
        #else:
            #spellCheckBool = True
#------------------------------------------------------------------------------
#randomSpellCheck() 
#printTests() #prints the lists to the console
#print(soundOutList[0:4]) #prints the first four words to console for testing
#print(pronunciationList[0:4]) #prints the first four kana to console for
#print(levelOneWords)

addSpaceToWords()

with open("soundOutput.txt", "w", encoding='utf8') as file: #writes the words and kana to a new file
    file.write("level 1 words:\n")
    for i in range(len(levelOneWords)):
        file.write(f"{levelOneKana[i]} ・ {levelOneWords[i]}\n") #writes the level 1 words and kana to the file
    file.write("\nlevel 2 words:\n")
    for i in range(len(levelTwoWords)):
        file.write(f"{levelTwoKana[i]} ・ {levelTwoWords[i]}\n")
    file.write("\nlevel 3 words:\n")
    for i in range(len(levelThreeWords)):
        file.write(f"{levelThreeKana[i]} ・ {levelThreeWords[i]}\n")  
    file.write("\nlevel 4 words:\n")
    for i in range(len(levelFourWords)):
        file.write(f"{levelFourKana[i]} ・ {levelFourWords[i]}\n")
    file.write("\nlevel 5 words:\n")
    for i in range(len(levelFiveWords)):
        file.write(f"{levelFiveKana[i]} ・ {levelFiveWords[i]}\n")
    file.write("\n")