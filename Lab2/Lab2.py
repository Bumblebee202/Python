import os
import re


def ReadText(filePath: str) -> str:
    try:
        with open(filePath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filePath} was not found.")
    except IOError:
        print("Error: An error occurred while reading the file.")
    return None


def CountLines(text: str) -> int:
    lines = text.splitlines()
    return len(lines)

def CountWords(text: str) -> int:
    words = re.split("\\W+", text)
    return len(words)


def CountLetters(text: str) -> tuple[int, int]:
    lowerChars = 0
    upperChars = 0

    for symbol in text:
        if not symbol.isalpha():
            continue

        if symbol.isupper():
            upperChars += 1
        else:
            lowerChars += 1
    
    return (lowerChars, upperChars)


def CountDigits(text: str) -> int:
    count = 0

    for symbol in text:
        if symbol.isdigit():
            count += 1

    return count


def CountPunctuation(text: str) -> int:
    count = 0

    punctuation = ".,?!:;"

    for symbol in text:
        if symbol in punctuation:
            count += 1

    return count;


def GetLongestWord(text: str) -> str:
    words = re.split("\\W+", text)

    longestWord = words[0]
    size = len(longestWord)

    for word in words[1:]:
        wordSize = len(word)
        if wordSize > size:
            size = wordSize
            longestWord = word
    
    return longestWord


def GetWordsBySubstring(text: str, substring: str) -> set[str]:
    words = re.split("\\W+", text)
    result = set[str]()

    for word in words:
        truncatedWord = word[1:-1]
        if substring in truncatedWord:
            result.add(word)

    return result


def ExtractDigits(text: str) -> set[str]:
    strs = text.split(",")

    numbers = set[str]()

    for item in strs:
        item = item.strip()
        if item.isdigit():
            numbers.add(item)

    return numbers


def AddOrIncreaseValue(key: str, map: dict[str, int]):
    if not key in map:
        map[key] = 1
    else:
        map[key] += 1


def GetCountsOfDigits(text: str, numbers: set[str]) -> dict[str, int]:
    map = dict[str, int]()

    for symbol in text:
        if not symbol.isdigit():
            continue

        if symbol in numbers:
            AddOrIncreaseValue(symbol, map)

    return map


def GetCountsOfWords(text: str, chars: set[str]) -> dict[str, int]:
    words = re.split("\\W+", text)
    map = dict[str, int]()

    minSize = 2

    for word in words:
        if len(word) < minSize:
            continue

        charsCount = 0

        for char in chars:
            if char in word:
                charsCount += 1

            if charsCount >= minSize:
                AddOrIncreaseValue(word, map)
                break

    return map

def Count(arr: list[any], value: any) -> int:
    count = 0

    for item in arr:
        if item == value:
            count += 1

    return count

def WordsmoreFrequentInFirstHalf(text: str):
    words = re.split("\\W+", text)

    middle = int(len(words) / 2)

    result = set[str]()

    firstHalf = words[0:middle + 1]
    secondHalf = words[middle + 1:]

    for word in firstHalf:
        if word in result:
            continue

        firstHalfCount = Count(firstHalf, word)
        secondHalfCount = Count(secondHalf, word)

        if firstHalfCount >= secondHalfCount:
            result.add(word)

    return result


def FindWord(text: str, word: str, ignoreCase: bool = True) -> list[tuple[int, str]]:
    lines = text.splitlines()
    result = list[(int, str)]()

    if ignoreCase == True:
        word = word.lower()

    index = 0
    for line in lines:
        lineValue = line
        if ignoreCase == True:
            lineValue = lineValue.lower()

        if word in lineValue:
            result.append((index, line))

        index += 1

    return result
    

# 22 % 4 + 1 (3)
direcoty = os.getcwd()
fileName = "tfotr.txt"

filePath = os.path.join(direcoty, fileName) 

fileContent = ReadText(filePath)

#Task 1
print(f"Lines count: {CountLines(fileContent)}") 
print(f"Words count: {CountWords(fileContent)}")
(lowerChars, upperChars) = CountLetters(fileContent)

print(f"Uppercase letters count: {upperChars}")
print(f"Lowercase letters count: {lowerChars}")
print(f"Total letters count: {lowerChars + upperChars}")

print(f"Digigts count: {CountDigits(fileContent)}")
print(f"Punctuation count: {CountPunctuation(fileContent)}")
print(f"Longest word is '{GetLongestWord(fileContent)}'")

# userInput = input("a. Input the text: ")
# print(GetWordsBySubstring(fileContent, userInput))

# userInput = input("b. Input digits separated by commas: ")
# digits = ExtractDigits(userInput)
# print(GetCountsOfDigits(fileContent, digits))

# userInput = input("c. Input the text: ")
# searchSymbol = { s for s in userInput }
# print(GetCountsOfWords(fileContent, searchSymbol))

# print("d. ", WordsmoreFrequentInFirstHalf(fileContent))
userInput = input("e. Input the word: ")
lines = FindWord(fileContent, userInput)
if len(lines) == 0:
    print("Empty")
else:
    for line in lines:
        print(f"{line[0]}: {line[1]}")