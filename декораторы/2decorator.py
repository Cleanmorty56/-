def superhero_p(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@superhero_p
def greet(superhero):
    print(f"Алоха, {superhero}!")

greet("ЖЧ")