from e2k import P2K, C2K
from g2p_en import G2p # any g2p library with CMUdict will work

wordList = []
kanaList = []

# cmudict phoneme to katakana
p2k = P2K()

g2p = G2p()

with open('wordsToKana.txt', 'r') as file: #reads file with however many words
    for line in file:
        wordList.append(line.strip().split("\t"))

def makeKana(): #function to take list in and make words katakana
     #copies the word list to kana list
    for i in range(len(wordList)):
        katakanaize = p2k(g2p(*wordList[i]))
        kanaList.append(katakanaize)
    
    return kanaList

makeKana()

#print(kanaList)
#print(wordList)

with open('kanaOutput.txt', 'w', encoding = 'utf8') as file: #writes kana to file
    for i in range(len(kanaList)):
        file.write(f"{kanaList[i]}  -  {wordList[i]}\n") #writes kana and word to file, separated by a dash