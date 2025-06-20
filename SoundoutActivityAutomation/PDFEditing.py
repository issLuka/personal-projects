#This is a program to automate creating lined a sound out activity I use for teaching
#Louis Faunce - made 06/20/2025
import random

inputFile = open("SoundOutInput.txt") #read input file with words
print(inputFile.read()) #test if can read

soundOutLines = inputFile.readlines() #variable to get specific lines (1-4 are level 1, 5-9 is 2 so on

levelOne = [soundOutLines[0], soundOutLines[1], soundOutLines[2], soundOutLines[3]] #array for level one words
#test if this works to make array of each line in text file

#close file
inputFile.close()

#function class to run randomizing
def randomSpelling():

    return 0

#function for making words into katakana
def katakanaize():

    return 0 

#loop to randomize every word in level output to levelXwordXjumbled or some, format with " " between each letter.

#loop to make version of each word katakana - output to  or something

#format for output to be sent to new file will be "kana ・ jumbled word"