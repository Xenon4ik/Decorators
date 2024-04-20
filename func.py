import requests
import re

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


def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@counter
@logging
@benchmark
def word_count(word, url='https://www.gutenberg.org/files/2638/2638-0.txt'):
    
    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub('[\W]+' , ' ', raw).lower()
    
    # считаем
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"

print(word_count('whole'))


@counter
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

fib(10)
