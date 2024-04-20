from functools import wraps
def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    memo = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if func.__name__ in memo:
          memo[func.__name__] += 1
        else:
          memo[func.__name__] = 1
        print(f'Функция была вызвана {memo[func.__name__]} раз')
        return result
    return wrapper