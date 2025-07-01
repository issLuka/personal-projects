from e2k import P2K, C2K
from g2p_en import G2p # any g2p library with CMUdict will work

wordsList = []
kanaList = []

# cmudict phoneme to katakana
p2k = P2K()

g2p = G2p()

with open('wordsToKana.txt', 'r') as file: #reads file with however many words
    for line in file:
        wordList = wordList.append(line.strip().split('\t'))

def makeKana(list): #function to take list in and make words katakana

    for i in range(list):
        katakanaize = p2k(g2p(*list[i]))
        kanaList.append(katakanaize)
    
    return kanaList

makeKana(wordList)

with open('kanaOutput.txt', 'w', encoding = 'utf8') as file: #writes to new file
    for i in range(len(kanaList)):
        file.write(kanaList[i], '\n')
    