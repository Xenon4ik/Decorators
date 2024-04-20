def memo(func):
  """
  Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
  """
  cache = {}

  def fmemo(x):
    if x in cache:
      print ('cached return')
      return cache[x]
    
    result = func(x)
    cache[x] = result
    print (f'not cached return with arg {x}')
    return result

  fmemo.cache = cache
  return fmemo