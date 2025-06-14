import functools

def LimitCalls(limit):
    callCount = 0

    def LimitDecorator(func):

        @functools.wraps(func)
        def LimitWrapper(*args, **kwargs):

            nonlocal callCount

            if callCount >= limit:
                raise RuntimeError(
                    f"Функція '{func.__name__}' викликана занадто багато разів! "
                    f"Дозволено {limit} викликів, але було {callCount + 1}."
                )
            
            callCount += 1
            print(f"Виклик '{func.__name__}' #{callCount}/{limit}")
            return func(*args, **kwargs)
        return LimitWrapper
    
    return LimitDecorator