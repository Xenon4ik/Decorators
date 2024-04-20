from functools import wraps
def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper