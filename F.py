####################################################

# F. Декоратор для замера времени выполнения методов

####################################################

import functools
import time

def time_measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Метод {func.__name__!r} выполнен за {end_time - start_time:.4f} сек.")
        return result
    return wrapper
