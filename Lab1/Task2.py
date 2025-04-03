import re
import math

def _GetSymbolIndexes(str, symbol):
    indexes = []
    start = 0

    while True:
        index = str.find(symbol, start)

        if index == -1:
            break

        start = index + 1
        indexes.append(index)

    return indexes

def _CustomJoin(str):
    size = 4
    strLen = len(str)
    substrLen = math.floor(strLen / size)
    print("len:", strLen, "str new len:", substrLen)

    substrs = []
    index = 0
    for iteration in range(size):
        if iteration < size - 1:
            subStr = str[index:index + substrLen]
        else :
            subStr = str[index:]

        substrs.append(subStr)
        index += substrLen

    newStr = ""

    for iteration in range(size - 1, -1, -1):
        if iteration % 2 == 0:
            newStr = newStr + substrs[iteration].lower()
        else:
            newStr = newStr + substrs[iteration].upper()

    return newStr

def _Max(words):
    max = len(words[0])

    for word in words[1:]:
        wordLen = len(word)
        
        if (wordLen > max):
            max = wordLen
    
    return max

def Task():
    # https://www.reddit.com/r/learnpython/comments/fwhcas/whats_the_difference_between_and_is_not/#:~:text=In%20Python%2C%20%3D%3D%20checks%20for,there%20is%20only%20NoneType%20instance.
    s = "To take a non programming approach, suppose you and I both have a $50 bill. They are of equal value but are not the same as their serial numbers differ.\nSo they are equivalent but not identical.\nIn Python, == checks for equivalency. For custom classes you can implement this yourself. In contrast, is and is not checks to see if two things are identical. Generally it's used to check if two variable names are aliases of each other and to check for None as there is only NoneType instance."
    # s = "abc123456qwe2"
    print(s)
    
    #1. Виведіть на екран довжину рядка
    print("1.")
    print(len(s))

    #2. Виведіть на екран символ, який знаходиться на позиції, яка дорівнює вашому варіанту.
    #Виведіть тип даних цього символу (`type()`).
    print("\n2.")
    print(s[22])
    print(type(s[22]))

    # #3. Виведіть на екран символ, який знаходиться на позиції вашого варіанту, якщо рахувати з кінця рядка.
    print("\n3.")
    print(s[-23])

    # #4. Виведіть всі символи рядка, починаючи від номеру вашого варіанта і до кінця рядка.
    print("\n4.")
    print(s[22:])

    # #5. Отримайте три останні символи рядка як один рядок та виведіть на екран.
    print("\n5.")
    print(s[-3:])

    # #6. Введіть символ з клавіатури. Перевірте чи рядок `s` містить цей символ (оператор `in`).
    # #Якщо так, виведіть відповідне повідомлення.
    print("\n6.")
    symbol = input("Input the symbol: ")
    print("Has string symbol:", symbol in s)

    # #7. Введіть символ з клавіатури. Виведіть на екран всі індекси входження цього символа в рядок `s` (`str.find(what, start, end)`) та кількість цих входжень.
    print("\n7.")
    symbol = input("Input the symbol again: ")
    indexes = _GetSymbolIndexes(s, symbol)
    print("Indexes:", indexes)
    print("Count:", len(indexes))

    # #8. Введіть рядок з клавіатури, та отримайте з рядка `s` новий рядок, замінивши в ньому введений рядок на символ `?` (`s.replace()`).
    print("\n8.")
    valueToReplace = input("Input value to replace: ")
    newStr = s.replace(valueToReplace, "?")
    print("new string:", newStr)

    # #9. Отримайте новий рядок, прибравши з рядка `s` всі розділові знаки.
    print("\n9.")
    strWithoutDelimeters = re.sub("[^a-zA-Z0-9 ]", "", s)
    print(strWithoutDelimeters)


    #10. Розбийте рядок `s` на 4 приблизно рівні частини. Об'єднайте ці частини в один рядок в зворотньому порядку (4, 3, 2, 1).
    #При цьому рядки 4 та 2 мають входити у верхньому регістрі (великі літери), а 1 та 3 у нижньому (маленькі літери).
    #Наприклад: `alpha beta gamma theta` $\to$ `THETA gamma BETA alpha`
    print("\n10.")
    print(_CustomJoin(s))

    #11. Введіть з клавіатури рядок, який міг би позначати ім'я файлу з розришенням, наприклад `lab.ipynb`.
    #Перевірте чи є цей файл виконуваним файлом Windows (має розширення `.exe`) та виведіть відповідне повідомлення.
    #Використовуйте функцію `str.endswith()` та конструкцію `if-else`.
    print("\n11.")
    fileName = input("Input the file name and extension: ")
    if fileName.endswith(".exe"):
        print("Looks like it's exe file")
    else:
        print("Looks like it's not exe file")

    #12. Розбийте рядок `s` на слова, виведіть кількість слів та довжину найдовшого слова (використовуйте цикл `for`).
    print("\n11.")
    words = s.split()
    print(len(words))
    print(_Max(words))