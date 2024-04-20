import time
from functools import wraps

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter() 
        result = func(*args, **kwargs)
        end = time.perf_counter() 
        print(f'{func.__name__} потребовалось {end - start:.6f} секунд')
        return result
    return wrapper