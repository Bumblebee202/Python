import Task1
import Task2


def SumExamples():
    print(f"SumAll(1, 2, 3): {Task1.SumAll(1, 2, 3)}")
    print(f"SumAll(10, 20): {Task1.SumAll(10, 20)}")
    print(f"SumAll(5): {Task1.SumAll(5)}")
    print(f"SumAll(0.5, 1.5, 2.2): {Task1.SumAll(0.5, 1.5, 2.2)}")
    print(f"SumAll(-1, 0, 1): {Task1.SumAll(-1, 0, 1)}")
    numbers1 = [100, 200, 300]
    print(f"SumAll({numbers1}): {Task1.SumAll(*numbers1)}")
    numbers2 = (1.1, 2.2, 3.3, 4.4)
    print(f"SumAll( {numbers2} ): {Task1.SumAll(*numbers2)}")
    listPart = [5, 6]
    print(f"SumAll(1, 2, *{listPart}, 7): {Task1.SumAll(1, 2, *listPart, 7)}")
    print("\n\n")


def AvgExamples():
    print(f"Average(1, 2, 3, 4, 5): {Task1.Average(1, 2, 3, 4, 5)}")
    print(f"Average(10, 20): {Task1.Average(10, 20)}")
    print(f"Average(7): {Task1.Average(7)}")
    print(f"Average(1.5, 2.5, 3.8): {Task1.Average(1.5, 2.5, 3.8)}")
    print(f"Average(-1, 0, 1): {Task1.Average(-1, 0, 1)}")
    print(f"Average(-1, 2, -3, 4, ignoreNegatives=True): {Task1.Average(-1, 2, -3, 4, ignoreNegatives=True)}") 
    print(f"Average(-5, -10, 0, ignoreNegatives=True): {Task1.Average(-5, -10, 0, ignoreNegatives=True)}")
    print(f"Average(-1, -2, -3, ignoreNegatives=True): {Task1.Average(-1, -2, -3, ignoreNegatives=True)}")
    data1 = [10, 20, 30]
    print(f"Average({data1}): {Task1.Average(*data1)}")
    data2 = (-5, 15, -25, 35)
    print(f"Average({data2}, ignoreNegatives=True): {Task1.Average(*data2, ignoreNegatives=True)}")
    listNums = [2, -4]
    print(f"Average(1, *{listNums}, 5, ignoreNegatives=False): {Task1.Average(1, *listNums, 5)}")
    print(f"Average(1, *{listNums}, 5, ignoreNegatives=True): {Task1.Average(1, *listNums, 5, ignoreNegatives=True)}")
    print("\n\n")


def ConcatExamples():
    print(f"Concatenate(\"Привіт\", \"світ\"): {Task1.Concatenate("Привіт", "світ")}")
    print(f"Concatenate(\"Один\", \"два\", \"три\"): {Task1.Concatenate("Один", "два", "три")}")
    print(f"Concatenate(\"Hello\"): {Task1.Concatenate("Hello",)}")
    print(f"Concatenate(): {Task1.Concatenate()}")
    print(f"Concatenate(\"Яблук\", \"Банан\", \"Апельсин\", separator=\", \"): {Task1.Concatenate("Яблуко", "Банан", "Апельсин", separator=", ")}")
    print(f"Concatenate(\"Path\", \"to\", \"file\", separator=\"/\"): {Task1.Concatenate("Path", "to", "file", separator="/")}")
    print(f"Concatenate(\"First\", \"Second\", separator=\"-\"): {Task1.Concatenate("First", "Second", separator="-")}")
    print(f"Concatenate(\"A\", \"B\", \"C\", separator=\"\"): {Task1.Concatenate("A", "B", "C", separator="")}")
    print(f"Concatenate(\"Alpha\", 123, \"Beta\", True, \"Gamma\"): {Task1.Concatenate("Alpha", 123, "Beta", True, "Gamma")}")
    print(f"Concatenate(1, 2, \"Число\", 3.14, \"Рядок\", [1,2]): {Task1.Concatenate(1, 2, "Число", 3.14, "Рядок", [1,2])}")
    words1 = ["Python", "is", "fun"]
    print(f"Concatenate({words1}): {Task1.Concatenate(*words1)}")
    words2 = ("Hello", "World", "!")
    print(f"Concatenate({words2}, separator=\"-\"): {Task1.Concatenate(*words2, separator="-")}")
    mixedList = ["Start", 123, "Middle", False, "End"]
    print(f"Concatenate({mixedList}, separator=\"_\"): {Task1.Concatenate(*mixedList, separator="_")}")
    print("\n\n")


def SumInExamples():
    print(f"SummIn(1, 5, 1, 2, 3, 4, 5): {Task1.SummIn(1, 5, 1, 2, 3, 4, 5)}")
    print(f"SummIn(10, 20, 5, 15, 25): {Task1.SummIn(10, 20, 5, 15, 25)}")
    print(f"SummIn(0, 10, 10, 0, 5): {Task1.SummIn(0, 10, 10, 0, 5)}")
    print(f"SummIn(-5, 5, -10, -3, 0, 3, 10): {Task1.SummIn(-5, 5, -10, -3, 0, 3, 10)}")
    print(f"SummIn(1.0, 3.0, 1.0, 1.5, 2.0, 2.5, 3.0): {Task1.SummIn(1.0, 3.0, 1.0, 1.5, 2.0, 2.5, 3.0)}") 
    print(f"SummIn(0.1, 0.9, 0.05, 0.5, 0.95): {Task1.SummIn(0.1, 0.9, 0.05, 0.5, 0.95)}")
    print(f"SummIn(1, 5, 1, \"two\", 3, None, 5): {Task1.SummIn(1, 5, 1, "two", 3, None, 5)}")
    print(f"SummIn(0, 10, \"text\", [1,2], 5, 15): {Task1.SummIn(0, 10, "text", [1,2], 5, 15)}")
    data1 = [1, 5, 10, 15, 20]
    print(f"SummIn(10, 20, {data1}): {Task1.SummIn(10, 20, *data1)}")
    data2 = (0.5, 1.5, 2.5, "bad", 3.5)
    print(f"SummIn(1.0, 3.0, {data2} ): {Task1.SummIn(1.0, 3.0, *data2)}")
    print("\n\n")


def FilterEvenExamples():
    print(f"FilterEven(1, 2, 3, 4, 5, 6): {Task1.FilterEven(1, 2, 3, 4, 5, 6)}")
    print(f"FilterEven(10, 20, 30): {Task1.FilterEven(10, 20, 30)}")
    print(f"FilterEven(7, 9, 11): {Task1.FilterEven(7, 9, 11)}")
    print(f"FilterEven(0, -2, -4): {Task1.FilterEven(0, -2, -4)}")
    print(f"FilterEven(2): {Task1.FilterEven(2)}")
    print(f"FilterEven(): {Task1.FilterEven()}")
    print(f"FilterEven(1, \"два\", 3, 4.0, \"п`ять\", 6): {Task1.FilterEven(1, "два", 3, 4.0, "п`ять", 6)}")
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"FilterEven({numbers1}): {Task1.FilterEven(*numbers1)}")
    mixedData = (10, 'abc', 20, 30.5, 40, [50])
    print(f"FilterEven( {mixedData} ): {Task1.FilterEven(*mixedData)}")
    print("\n\n")


def DisplayInfoExamples():
    Task2.DisplayInfo(firstName="Yura", lastName="Сидоров")
    Task2.DisplayInfo(product="Ноутбук", price=1200.50, currency="USD", brand="Acer")
    Task2.DisplayInfo(id=1, status="active")
    userData = {"username": "user123", "email": "user@example.com", "isActive": True}
    Task2.DisplayInfo(**userData)
    itemDetails = {"itemId": "A123", "quantity": 5, "location": "Warehouse B"}
    Task2.DisplayInfo(category="Electronics", **itemDetails, weight="2kg")
    emptyDict = {}
    Task2.DisplayInfo(**emptyDict)
    print("\n\n")


def FilterKwargsExamples():
    print(f"FilterKwargs(name=\"Yura\", age=25, city=\"Odesa\"): {Task2.FilterKwargs(name="Yura", age=25, city="Odesa")}")
    print(f"FilterKwargs(item='\"Laptop\", price=1200, weight=1.8): {Task2.FilterKwargs(item='Laptop', price=1200, weight=1.8)}")
    print(f"FilterKwargs(num1=10, num2=20): {Task2.FilterKwargs(num1=10, num2=20)}")
    print(f"FilterKwargs(name=\"Bob\", city=\"Lviv\", status=True): {Task2.FilterKwargs(name='Bob', city='Lviv', status=True)}")
    data1 = {"id": 101, "name": "Product A", "quantity": 5, "price": 99.99}
    print(f"FilterKwargs({data1}): {Task2.FilterKwargs(**data1)}")
    data2 = {"status": "completed", "error": None}
    print(f"FilterKwargs({data2}): {Task2.FilterKwargs(**data2)}")
    print("\n\n")


def MergeDictsExamples():
    dictA = {"name": "Yura", "age": 25}
    dictB = {"city": "Odesa", "occupation": "Developer"}
    print(f"MergeDicts({dictA},{dictB}): {Task2.MergeDicts(firstDict=dictA, secondDict=dictB)}")

    dictA = {"fruit": "apple", "color": "red", "quantity": 5}
    dictB = {"color": "green", "price": 1.5, "quantity": 10}
    print(f"MergeDicts({dictA}, {dictB}): {Task2.MergeDicts(firstDict=dictA, secondDict=dictB)}")

    dictA = {}
    dictB = {"id": 123}
    print(f"MergeDicts({dictA}, {dictB}): {Task2.MergeDicts(firstDict=dictA, secondDict=dictB)}")

    dictA = {"val1": 1, "val2": "hello"}
    dictB = {"val2": True, "val3": [1, 2]}
    print(f"MergeDicts({dictA}, {dictB}): {Task2.MergeDicts(firstDict=dictA, secondDict=dictB)}")
    print("\n\n")

def CountTypesExamples():
    print(f"CountTypes(a=1, b='hello', c=3.14, d=True, e=[1, 2]): {Task2.CountTypes(a=1, b='hello', c=3.14, d=True, e=[1, 2])}")
    print(f"CountTypes(name='Іван', age=25, city='Львів', postcode='79000'): {Task2.CountTypes(name='Іван', age=25, city='Львів', postcode='79000')}")
    print(f"CountTypes(x=10, y=20, z=30): {Task2.CountTypes(x=10, y=20, z=30)}")
    userProfile = {
    "username": "user1",
    "id": 123,
    "email": "user@example.com",
    "isActive": True,
    "lastLogin": None,
    "interests": ["coding", "reading"]
    }
    print(f"CountTypes({userProfile}): {Task2.CountTypes(**userProfile)}")
    print("\n\n")


def ValidateUser():
    user1 = {"username": "user123", "email": "test@example.com", "password": "strong_password123"}
    print(f"Task2.ValidateUser({user1}): {Task2.ValidateUser(**user1)}")

    user2 = {"username": "usr", "email": "usr@test.com", "password": "long_password"}
    print(f"ValidateUser({user2}): {Task2.ValidateUser(**user2)}")

    user3 = {"username": "testuser", "email": "test.com", "password": "secure_password"}
    print(f"Валідація {user3}: {Task2.ValidateUser(**user3)}")




# 1.1.
SumExamples()

# 1.2.
AvgExamples()

# 1.3.
ConcatExamples()

# 1.4.
SumInExamples()

# 1.5.
FilterEvenExamples()

# 2.1
DisplayInfoExamples()

# 2.2
FilterKwargsExamples()

# 2.3
MergeDictsExamples()

# 2.4
CountTypesExamples()

# 2.5
ValidateUser()