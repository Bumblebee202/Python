def DisplayInfo(**kwargs):
    if not kwargs:
        return

    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    print("\n")


def FilterKwargs(**kwargs) -> str:
    filteredItems = []
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            filteredItems.append(f"{key}({value})")
    
    if not filteredItems:
        return ""

    return ", ".join(filteredItems)

def MergeDicts(**kwargs):
    if len(kwargs) != 2:
        raise ValueError("Функція MergeDicts повинна приймати рівно два іменованих аргументи (два словники).")

    dictValues = list(kwargs.values())

    dict1 = dictValues[0]
    dict2 = dictValues[1]

    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Обидва аргументи повинні бути словниками.")

    resultDict = dict1.copy()
    resultDict.update(dict2)

    return resultDict


def CountTypes(**kwargs):
    typeCounts = {}
    for value in kwargs.values():
        
        typeName = type(value).__name__
        typeCounts[typeName] = typeCounts.get(typeName, 0) + 1
        
    return typeCounts


def ValidateUser(**kwargs):
    validationResults = {
        "username": False,
        "email": False,
        "password": False,
        "isValid": True 
    }

    requiredFields = ["username", "email", "password"]
    for field in requiredFields:
        if field not in kwargs:
            print(f"Помилка: Відсутнє обов'язкове поле '{field}'.")
            validationResults[field] = False
            validationResults["isValid"] = False

    username = kwargs.get("username")
    if isinstance(username, str) and len(username) > 3:
        validationResults["username"] = True
    else:
        if username is not None:
            print(f"Помилка валідації username: '{username}' має бути рядком і довжиною > 3 символів.")
        validationResults["isValid"] = False

    email = kwargs.get("email")
    if isinstance(email, str) and "@" in email:
        validationResults["email"] = True
    else:
        if email is not None:
            print(f"Помилка валідації email: '{email}' має бути рядком і містити символ '@'.")
        validationResults["isValid"] = False

    password = kwargs.get("password")
    if isinstance(password, str) and len(password) > 8:
        validationResults["password"] = True
    else:
        if password is not None:
            print(f"Помилка валідації password: '{password}' має бути рядком і довжиною > 8 символів.")
        validationResults["isValid"] = False
    
    return validationResults