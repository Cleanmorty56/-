def messenger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов этой функции: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

@messenger
def greet(message):
    print(f"Это {message} из далекого будущего ")


greet("сообщение")
