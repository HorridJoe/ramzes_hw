from functools import wraps


def log(filename=""):
    """
    Декоратор для логирования работы функции в текстовый файл
    :param filename:
    :return:
    """

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename != "":
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as err:
                if filename != "":
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {err}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {err}. Inputs: {args}, {kwargs}")

        return inner

    return wrapper
