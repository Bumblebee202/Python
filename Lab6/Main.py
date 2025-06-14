from Task1 import MeasureRegularFunc, MeasureWithoutWraps, Measure
from Task2 import LimitCalls
from Task3 import Repeat
import time

def LongRunningFunction(duration: int, message:str = "Завершено"):
    print(f"Починаємо виконання на {duration} секунд...")
    time.sleep(duration)
    print(message)
    return f"Завдання тривалістю {duration} секунд виконано успішно."


@MeasureWithoutWraps
def LongRunningFunction2(duration, message="Завершено"):
    print(f"Починаємо виконання на {duration} секунд...")
    time.sleep(duration)
    print(message)
    return f"Завдання тривалістю {duration} секунд виконано успішно."


@Measure
def LongRunningFunction3(duration, message="Завершено"):
    print(f"Починаємо виконання на {duration} секунд...")
    time.sleep(duration)
    print(message)
    return f"Завдання тривалістю {duration} секунд виконано успішно."


@LimitCalls(10)
def Send(request: str):
    time.sleep(0.5)


@Repeat(times=3)
def ReadInt(message: str) -> int:
    try:
        value = int(input(message))
        return value
    except ValueError:
        print("Некоректний ввід! Будь ласка, введіть ціле число.")
        raise 


# 1
# @Measure
# @Repeat(times=3)
# 2
@Repeat(times=3)
@Measure
def ReadInt2(message: str) -> int:
    try:
        value = int(input(message))
        return value
    except ValueError:
        print("Некоректний ввід! Будь ласка, введіть ціле число.")
        raise

print(f"Результат MeasureRegularFunc: {MeasureRegularFunc(LongRunningFunction, 2)}\n\n")


print(f"Результат LongRunningFunction2: {LongRunningFunction2(2, message="Моє довге завдання завершено!")}\n\n")


print(f"Результат LongRunningFunction3: {LongRunningFunction3(2, message="Моє довге завдання завершено!")}\n\n")


for i in range(9): # 9 calls
    Send("some request") # OK

    Send("some other request") # OK 10-th call
    try:
        Send("some other request")
    except RuntimeError as e:
        print(e)

        
print("Введіть число")
try:
    num = ReadInt("Введіть ціле число: ")
    print(f"Ви ввели число: {num}")
except ValueError as e:
    print(f"Не вдалося прочитати ціле число після всіх спроб: {e}")
except Exception as e:
    print(f"Виникла несподівана помилка: {e}")

print("Введіть число")
try:
    num = ReadInt2("Введіть ціле число: ")
    print(f"Ви ввели число: {num}")
except ValueError as e:
    print(f"Не вдалося прочитати ціле число після всіх спроб: {e}")
except Exception as e:
    print(f"Виникла несподівана помилка: {e}")