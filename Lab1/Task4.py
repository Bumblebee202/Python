def Task():
    _Task1()
    _Task2()

def _Task1():
    #Виведіть ім'я та місто користувача, визначені в списках `names` та `cities`,
    #у вигляді таблиці:
    print("\n1.")

    names = [ 
    'Олександр', 'Анастасія', 'Володимир', 'Єлизавета','Наталія',
    'Дмитро', 'Ольга', 'Сергій', 'Ірина', 'Тетяна', 'Катерина',
    'Андрій', 'Марія', 'Юлія', 'Максим', 'Вікторія', 'Тимур', 
    'Олександра', 'Софія', 'Роман'
    ]

    cities = [
        'Київ', 'Львів', 'Одеса', 'Дніпро', 'Харків',
        'Запоріжжя', 'Кривий Ріг', 'Миколаїв', 'Вінниця', 'Донецьк',
        'Івано-Франківськ', 'Чернівці', 'Полтава', 'Суми', 'Тернопіль', 
        'Рівне', 'Житомир', 'Черкаси', 'Хмельницький', 'Луцьк'
    ]
    
    hline = "".join(['-'] * 45)

    header: str = f"{"Ім`я":^22} {"Місто":^22}"

    size: int = len(cities)

    print(hline)
    print(header)
    print(hline)

    for index in range(size):
        name: str = names[index]
        city: str = cities[index]

        print(hline)
        line: str = f"|{name:^21}|{city:^21}|"
        print(line)

def _Task2():
    #Виведіть таблицю констант $\pi = 3.14159265359$, $e = 2.71828182846$, $\phi = 1.61803398875$
    #з різною точністю та вирівнюванням відповідно до вашого варіанту (номер завдання = номер варіанту % 5 + 1)

    # taskNumber: int = 22 % 5 + 1 #(3)
    # 3. З точністю до 5 знаків після крапки, ширина поля 15, вирівнювання по центру,
    
    print("\n2.")

    separator: str = "".join(['-'] * 49)

    pi: float = 3.14159265359
    e: float = 2.71828182846
    phi: float = 1.61803398875

    

    table: list[str] = []
    table.append(separator)
    table.append(f"|{"π":^15}|{"e":^15}|{"φ":^15}|")
    table.append(separator)
    table.append(f"|{pi:^15.5f}|{e:^15.5f}|{phi:^15.5f}|")
    table.append(separator)

    for line in table:
        print(line)
