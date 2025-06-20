#This is a program to automate creating lined a sound out activity I use for teaching
#Louis Faunce - made 06/20/2025
import random

soundOutList = [] #sets up list for words

with open("stink.txt", "r") as file: #reads file and puts to list, removing whitespace. "r" is for read only
    for line in file:
        soundOutList.append(line.strip().split("\t")) #formats the words into the list (use * when printing or writing to new file to remove [""]

#function class to run randomizing
def randomSpelling():
    print(''.join(random.sample(*soundOutList[1],len(*soundOutList[1])))) #edit to use loop and edit each string within the list
    return 0

#function for making words into katakana
def katakanaize():

    return 0 

#loop to randomize every word in level output to levelXwordXjumbled or some, format with " " between each letter.

#loop to make version of each word katakana - output to  or something

#format for output to be sent to new file will be "kana ・ jumbled word"
