from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("".join([f"{func.__name__}({arg}: {type(arg)}), " for arg in args]))
        print("".join([f"{func.__name__}({kw}: {type(kw)}), " for kw in kwargs]))
        return result
    return wrapper

@type_logger
def calc_degree(x, y):
    return x ** 3 + y

print(calc_degree(5, 8))
