import functools
import time

def Repeat(times):
    if not isinstance(times, int) or times < 1:
        raise ValueError("Параметр 'times' для декоратора repeat повинен бути цілим числом >= 1.")

    def RepeatDecorator(func):
        @functools.wraps(func)
        def RepeatWrapper(*args, **kwargs):
            lastException = None
            
            for attempt in range(1, times + 1):
                try:
                    print(f"Спроба {attempt}/{times} для функції '{func.__name__}'...")
                    result = func(*args, **kwargs)
                    print(f"Функція '{func.__name__}' успішно виконана на спробі {attempt}.")
                    return result
                except Exception as e:
                    lastException = e
                    print(f"Помилка на спробі {attempt} для '{func.__name__}': {e}")
                    if attempt < times:
                        time.sleep(0.5) 
                print("\n")
                
            if lastException:
                raise lastException
            else:
                raise RuntimeError(f"Функція '{func.__name__}' не змогла виконатись після {times} спроб без помилки.")
        
        return RepeatWrapper
    
    return RepeatDecorator