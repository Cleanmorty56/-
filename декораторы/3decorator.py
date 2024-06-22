def preobraz(func):
    def wrapper(*args, **kwargs):
        resultat = func(*args, **kwargs)
        return str(resultat)
    return wrapper

@preobraz
def plusik(a, b):
    return a + b

resultat = plusik(40, 12)
print(f" {resultat} Санкт-Петербург, тип данных: {type(resultat)}")