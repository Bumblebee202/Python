def Task():
    _Task1()
    _Task2()
    _Task3()
    _Task4()
    _Task5()
    _Task6()
    _Task7()
    _Task8()
    _Task9()
    _Task10()
    _Task11()
    

def _Task1():
    #1. Створіть пустий список за допомогою конструктора `list()` та зберіжіть його в змінній `data`. 
    #Додайте в нього такі елементи: ваше ім'я, прізвище, по-батькові, назву групи, номер групи (числом).
    #Виведіть тип `data` та кількість елементів списку. 
    #Для кожного елементу списку виведіть з нового рядка його тип, ідентифікатор та значення.
    print("\n1.")

    data = list()
    data.append("Юра")
    data.append("Сидоров")
    data.append("Максимович")
    data.append("АД")
    data.append(231)

    print(type(data), len(data))

    for item in data:
        print(type(item), id(item), item)

def _Task2():
    #2. Створіть список з 3 цілих чисел. Додайте в список новий елемент за допомогою функції `list.append()`. 
    #Перевірте, ми таким чином змінили список (залишився той самий об'єкт), чи створили новий?
    print("\n2.")
    numbers: list[int] = [1, 2, 3]
    print(id(numbers), len(numbers), numbers)

    numbers.append(4)
    print(id(numbers), len(numbers), numbers)

def _Task3():
    #3. Створіть два списки `a` та `b` з довільним вмістом. Об'єднайте їх за допомогою оператора `+`,
    #Результат збережіть в змінну `c`. Напишіть код, щоб дізнатись скільки різних об'єктів типу `list` ми тепер маємо?
    print("\n3.")
    a: list[int] = [1, 2, 3, 4]
    b: list[str] = ['one', 'two']
    c = a + b

    for item in c:
        print(id(item), type(item), item)

def _Task4():
    #4. Створіть список `x` з кількох цілих чисел. Додайте до нього нові елементи різними способами по черзі:
    #- `list.append()` (додавання одного елемента)
    #- `list.extend()` (додавання списку кількох елементів)
    #- оператор `+`  (тобто `x = x + [...]`)
    #- оператор `+=` (тобто `x += [...]`)
    #Після кожної такої дії виводьте ідентифікатор `id()` об'єкту, на який вказує `x`.\
    #Зробіть висновки, опишіть який спосіб змінює наявний список, а який створює новий.
    print("\n4.")
    x: list[int] = [1, 5]
    print(id(x))

    x.append(10)
    print(id(x))

    x.extend([2, 5])
    print(id(x))

    x = x + [1, 2, 3]
    print(id(x))

    x += [3, 2, 1]
    print(id(x))

def _Task5():
    #5. Створіть список `x` з кількох цілих чисел. Створіть нову змінну `a = x`. 
    #Створіть копію списку `x` та запишіть її в змінну `b`. Додайте в список `b` 
    #новий елемент за допомогою функції `list.append()`. 
    #Перевірте, ми таким чином змінили список `x`, `a` та `b`? Скільки окремих об'єктів списку маємо?
    print("\n5.")
    x: list[int] = [1, 2, 3]
    a: list[int] = x
    b: list[int] = x
    b.append(5)

    print('x:', x)
    print('a:', a)
    print('b:', b)

def _Task6():
    #6. Створіть два окремі об'єкти списку `[ 1, 2, 3 ]` і запишіть їх в змінні `x` та `y`.
    #Виведіть результат операцій `x is y`, `id(x)`, `id(y)`, `x == y` та опишіть результат.
    #Додайте в список `x` новий елемент за допомогою операції  `.append()`. Перевірте знов результат `x == y`.
    #Що на вашу думку робить цей вираз?
    print("\n6.")

    x: list[int] = [1, 2, 3]
    y: list[int] = [1, 2, 3]

    print('x is y ', x is y)
    print('x in y ', x in y)
    print('x == y', x == y)

    x.append(4)

    print('x == y', x == y)

def _Task7():
    #7. Створіть список з десяти цілих чисел за допомогою літералу списку `[ ... ]`.
    #За допомогою *одного* циклу виводьте почергово з нового рядка: перший елемент, потім перші два елементи,
    #потім перші три і так далі. Останній рядок має містити всі елементи списку.
    print("\n7.")

    numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    iteration: int = 1
    listSize: int = len(numbers)
    
    while iteration <= listSize:
        print(numbers[0:iteration])
        iteration += 1

def _Task8():
    #8. Повторіть попереднє завдання, тільки виводьте елементи починаючи з кінця списку.
    print("\n8.")

    numbers: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    iteration: int = 1
    listSize: int = len(numbers)
    startIndex: int = listSize - 1;

    #https://www.reddit.com/r/learnpython/comments/18p0jss/reversing_a_list_using_slice/
    while iteration <= listSize:
        print(numbers[startIndex::-1])
        startIndex -= 1
        iteration += 1
    
def _Task9():
    #9. В 20-поверховому будинку на кожному поверсі по 8 квартир. *На останньому поверсі всі квартири об'єднані в одну.*
    #Нумерація квартир починається з першого поверху з номера 1. Створіть програмно список, кожен $i$-елемент якого
    #буде списком номерів квартир $i$-поверху. Виведіть побудований список.
    #Виведіть номери квартир з 4 по 8 поверхи за допомогою зрізу (`list[:]`).
    print("\n9.")

    house: list[list[int]] = []
    size: int = 20
    index: int = 0

    flatNumber: int = 1
    flatsCount: int = 8

    while index < size:

        if index == size - 1:

            house.append([flatNumber])
            break

        else: 

            flats: list[int] = []
            house.append(flats)

            flatIndex: int = 0 
            while flatIndex < flatsCount:
                flatIndex += 1
                flats.append(flatNumber)
                flatNumber += 1

        index += 1
            
    for floor in house[4:8]:
        print(floor)


def _Task10():
    #10. Введіть українською мовою текстовий рядок з клавіатури за допомогою функції `input()`.\
    #Створіть список символів цього рядка за допомогою функцції `list()`. Видаліть зі списку усі\
    #голосні літери. З літер що залишились утворіть новий рядок. Для цього використовуйте функцію\
    #`str.join(list)`.Вона поєднує в один текстовий рядок елементри списку `list`, розділяючи їх текстом\
    #рядку `str`. Наприклад: `'+'.join(['a', 'b', 'c'])` $\to$ `'a+b+c'`.
    print("\n10.")

    userInput: str = input("Введіть текст: ")

    chars: list[str] = list(userInput)
    output: list[str] = []

    vowels: str = "аеєиіїоуюяАЕЄИІЇОУЮЯ"

    for char in chars:
        if char not in vowels:
            output.append(char)

    print("".join(output))


def _Task11():
    #11. Функція `list()` дозволяє створити новий список з іншої колекції даних, наприклад, з іншого списку.
    #Вона також дозволяє створити пустий список. Є різні способи створення пустого списку. 
    #Перевірте що роблять такі фрагменти коду та спробуйте описати результат:
    # - `[]`
    # - `list()`
    # - `[[]]`
    # - `[list()]`
    # - `list([])`
    # - `list(list())` 

    arr1 = []
    arr2 = list()
    twoDimensionalArr1 = [[]]
    twoDimensionalArr2 = [list()]
    twoDimensionalArr3 = list([])
    twoDimensionalArr4 = list(list())