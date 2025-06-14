def SumAll(*args) -> int | float:

    totalSum = 0
    for arg in args:

        if not isinstance(arg, (int, float)):
            raise TypeError(f"Нечисловий аргумент знайдено: {arg}. Всі аргументи повинні бути числами.")
            
        totalSum += arg            
    
    return totalSum


def Average(*args, ignoreNegatives=False) -> int | float:

    if not args:
        return 0.0

    validNumbers = []
    for arg in args:

        if not isinstance(arg, (int, float)):
            raise TypeError(f"Нечисловий аргумент знайдено: {arg}. Всі аргументи повинні бути числами.")
        
        if ignoreNegatives and arg < 0:
            continue
        
        validNumbers.append(arg)
    
    if not validNumbers:
        return 0.0

    return sum(validNumbers) / len(validNumbers)



def Concatenate(*args, separator=' ') -> str:

    validStrings = []
    for arg in args:
        if isinstance(arg, str):
            validStrings.append(arg)

    if not validStrings:
        return ""

    return separator.join(validStrings)


def SummIn(a: int | float, b: int | float, *args) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Параметри 'a' та 'b' повинні бути числами.")

    if a > b:
        temp = a
        a = b
        b = temp

    totalSum = 0.0
    for arg in args:
        
        if not isinstance(arg, (int, float)):
            continue

        if a <= arg <= b:
            totalSum += arg
            
    return totalSum


def FilterEven(*args):

    evenNumbers = []
    for arg in args:
        if isinstance(arg, int) and arg % 2 == 0:
            evenNumbers.append(arg)
            
    return evenNumbers