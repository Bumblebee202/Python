import os
import re
import random

def ReadText(filePath: str) -> str:
    try:
        with open(filePath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filePath} was not found.")
    except IOError:
        print("Error: An error occurred while reading the file.")
    return None


def ChooseWord(words: list[str], wordLen: int) -> str:
    wordSet = { word for word in words if len(word) == wordLen }

    randomIndex = random.randrange(0, len(wordSet) + 1)

    index = 0

    for word in wordSet:
        if index == randomIndex:
            return word.lower()
        index += 1

    return None


def OpenLetter(word: list[str], hiddenWord: list[str], letter: str):

    for index in range(0, len(word)):
        if word[index] == letter:
            hiddenWord[index] = letter


def Choise1(word: list[str], hiddenWord: list[str]):
    while True:
        randomIndex = random.randrange(0, len(hiddenWord) + 1)
        if hiddenWord[randomIndex] == "*":
            letter = word[randomIndex]
            hiddenWord[randomIndex] = letter

            break


def Choise2(word: list[str], hiddenWord: list[str]):
    hiddenWord[0] = word[0]


def Choise3(userLetters: set[str]):
    allLetters = "abcdefghijklmnopqrstuvwxyz"

    usedLetters = set[str]()

    count = 5

    while count > 0:
        randomIndex = random.randrange(0, len(allLetters) + 1)

        letter = allLetters[randomIndex]

        if letter in userLetters or letter in usedLetters:
            continue

        usedLetters.add(letter)
        count -= 1

    
    print(usedLetters)


def Choise(word: list[str], hiddenWord: list[str], userLetters: set[str]):
    choise = int(input("You can:\n1. Open random letter\n2. Open the first letter\n3. See 5 letter\n"))

    if choise == 1:
        Choise1(word, hiddenWord)
    elif choise == 2:
        Choise2(word, hiddenWord)
    elif choise == 3:
        Choise3(userLetters)
    else:
        raise Exception("Incorrect choise")
    


#Task2
direcoty = os.getcwd()
fileName = input("Enter one of them:\n 1. 'tfotr.txt'\n2. 'eneida.txt'\n3. 'alice.txt'\n")

filePath = os.path.join(direcoty, fileName) 

fileContent = ReadText(filePath)

if fileContent is None:
    print("GG")
    exit(0)

words = re.split("\\W+", fileContent)

wordSize = int(input("Enter word size: "))

word = ChooseWord(words, wordSize)
if word is None:
    print("GG")
    exit(0)

tries = int(wordSize * 1.5)
misses = 0
hiddenWord = ["*"] * wordSize
userInputs = set[str]()

while tries > 0 and "*" in hiddenWord:
    try:
        if misses == 3:
            Choise(word, hiddenWord, userInputs)
            misses = 0
            continue

        print(f"Tries: {tries}\nWord: '{hiddenWord}'")
        letter = input("Enter the letter: ").lower()


        if not letter.isalpha():
            print("It should be letter")
            continue

        if letter in userInputs:
            print(f"You have entered '{letter}'. Try again.")
            continue

        userInputs.add(letter)

        if letter not in word:
            tries -= 1
            misses += 1
            continue
        else:
            misses = 0
            OpenLetter(word, hiddenWord, letter)
    except:
        print("Error: try again")

if "*" in word:
    print("You lose")
else:
    print(f"You win: the word is '{word}'")
