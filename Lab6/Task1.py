import time
from functools import wraps

def MeasureRegularFunc(task, *args, **kwargs):
    startTime = time.perf_counter()

    result = task(*args, **kwargs)

    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    print(f"Функція '{task.__name__}' виконана за {elapsedTime:.4f} секунд.")
    
    return result

def MeasureWithoutWraps(func):

    def WrapperWithoutWraps(*args, **kwargs):
        startTime = time.perf_counter()
        result = func(*args, **kwargs)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        print(f"Функція '{func.__name__}' виконана за {elapsedTime:.4f} секунд.")
        return result
    
    return WrapperWithoutWraps

def Measure(func):
    @wraps(func)

    def wrapper(*args, **kwargs):
        startTime = time.perf_counter()
        result = func(*args, **kwargs)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        print(f"Функція '{func.__name__}' виконана за {elapsedTime:.4f} секунд.")
        return result
    
    return wrapper