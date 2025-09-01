def cache(func, history={}):
    def wrapper(*args):
        if args in history:
            print("Getting from cache")
            return history[args]
        else:
            print("Calculating new result")
            result = func(*args)
            history[args] = result
            return result
    return wrapper

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]