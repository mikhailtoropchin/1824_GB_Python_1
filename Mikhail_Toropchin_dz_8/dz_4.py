from functools import wraps


def logger(bool): # где аргумент - это функция, передаваемая в обертку
   def _logger(func):
       @wraps(func) # не понял как работает (может и не работает)
       def wrapper(*args):
           result = func(*args) # присваиваем переменную
           if bool(*args): # здесь смотрим на результат функции (True/False), переданной в обертку как аргумент
              return result
           else:
              for arg in args:
                 msg = f'wrong value: {arg}'
                 raise ValueError(msg) # возбуждаем(ся)
       return wrapper
   return _logger


@logger(lambda x: x > 0) # аргумент-функция возвращает True или False
def render_input(x):
   return x ** 3

print(render_input(2))
