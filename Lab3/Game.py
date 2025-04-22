import os
import random
import re
import copy

__all__ = ['Play', 'InitText', 'InitFromFiles', "GetStats", "ShowStats", "ClearStats"]

_words = set[str]()
_stats = []
_gameNumber = 0

def _ReadText(filePath: str) -> str:
    try:
        with open(filePath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filePath} was not found.")
    except IOError:
        print("Error: An error occurred while reading the file.")
    return ""

def _InitState(word: str, difficulty: int, attempts: int):
    global _gameNumber
    _gameNumber += 1

    stats = dict()
    stats["gameNumber"] = _gameNumber
    stats["word"] = word
    stats["difficulty"] = difficulty
    stats["attempts"] = attempts

    global _stats
    _stats.append(stats)

    
def _ChooseWord(wordLen: int) -> str:

    wordSet = { word for word in _words if len(word) == wordLen }

    randomIndex = random.randrange(0, len(wordSet) + 1)

    index = 0

    for word in wordSet:
        if index == randomIndex:
            return word.lower()
        index += 1

    return None

def InitText(text: str):
    words = re.split("\\W+", text)

    global _words
    _words = { word.lower() for word in words }

def InitFromFiles(files: list[str]):
    content = ""

    for file in files:
        content += _ReadText(file)

    InitText(content)

def Play(difficulty: int = 3):
    tuple = _InitGame(difficulty)

    if tuple is None:
        print("gg")
        return None
    
    (word, attempts) = tuple

    _InitState(word, difficulty, attempts)
    _StartGame(word, attempts)

def GetStats(count: int = 1) -> list[dict]:
    global _stats
    maps = _stats[-count:]

    return copy.deepcopy(maps)

def ShowStats(count: int = 0):
    global _stats
    maps = _stats[-count:]

    for map in maps:
        gameNumber = map["gameNumber"]
        word = map["word"]
        difficulty = map["difficulty"]
        attempts = map["attempts"]

        print(f"Game number: {gameNumber}.\nWord: '{word}'\nDifficulty: {difficulty}\nAttempts: {attempts}\n\n")

def ClearStats():
    global _stats
    _stats = list[dict]()

def _StartGame(word: str, attempts: int):

    wordSize = len(word)
    misses = 0
    hiddenWord = ["*"] * wordSize
    userInputs = set[str]()

    while attempts > 0 and "*" in hiddenWord:
        try:
            if misses == 3:
                _Choise(word, hiddenWord, userInputs)
                misses = 0
                continue

            print(f"Attempts: {attempts}\nWord: '{hiddenWord}'")
            letter = input("Enter the letter: ").lower()


            if not letter.isalpha():
                print("It should be letter")
                continue

            if letter in userInputs:
                print(f"You have entered '{letter}'. Try again.")
                continue

            userInputs.add(letter)

            if letter not in word:
                attempts -= 1
                misses += 1
                continue
            else:
                misses = 0
                _OpenLetter(word, hiddenWord, letter)
        except:
            print("Error: try again")

    if "*" in hiddenWord:
        print("You lose")
    else:
        print(f"You win: the word is '{word}'")

def _OpenLetter(word: list[str], hiddenWord: list[str], letter: str):

    for index in range(0, len(word)):
        if word[index] == letter:
            hiddenWord[index] = letter

def _InitGame(difficulty: int) -> tuple[str, int]:
    if difficulty < 1 or difficulty > 5:
        return None
    
    minLen = 3
    maxLen = 5
    attempts = 15

    for index in range(difficulty + 1):
        attempts = int(round(attempts * 0.8, 2))
        if index + 1 == 1:
            continue

        minLen = int(round(minLen * 1.2, 2))
        maxLen = int(round(maxLen * 1.2, 2))

    wordLen = random.randrange(minLen, maxLen + 1)

    word = _ChooseWord(wordLen)

    if word is None or len(word.strip()) == 0:
        return None;

    return (word, attempts)

def _Choise1(word: list[str], hiddenWord: list[str]):
    while True:
        randomIndex = random.randrange(0, len(hiddenWord) + 1)
        if hiddenWord[randomIndex] == "*":
            letter = word[randomIndex]
            hiddenWord[randomIndex] = letter

            break

def _Choise2(word: list[str], hiddenWord: list[str]):
    hiddenWord[0] = word[0]

def _Choise3(userLetters: set[str]):
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

def _Choise(word: list[str], hiddenWord: list[str], userLetters: set[str]):
    choise = int(input("You can:\n1. Open random letter\n2. Open the first letter\n3. See 5 letter\n"))

    if choise == 1:
        _Choise1(word, hiddenWord)
    elif choise == 2:
        _Choise2(word, hiddenWord)
    elif choise == 3:
        _Choise3(userLetters)
    else:
        raise Exception("Incorrect choise")


if __name__ == "__main__":
    files = ["alice.txt", "tfotr.txt"]
    InitFromFiles(files)
    Play()
    ShowStats(0)