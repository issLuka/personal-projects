from e2k import P2K, C2K
from g2p_en import G2p # any g2p library with CMUdict will work

testList = ["phone", "cat", "dog", "elephant", "computer", "drum", "guitar", "piano", "violin", "flute"]

# cmudict phoneme to katakana
p2k = P2K()

g2p = G2p()

word = "the" # track 2 from Aphex Twin's "Drukqs"
katakana = p2k(g2p(word))

katakanaListTest = p2k(g2p(testList[1]))

print(katakana) # "ボードヒッチン"

print(katakanaListTest) # "キャット"