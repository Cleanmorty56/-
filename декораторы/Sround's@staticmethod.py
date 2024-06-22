class Circle:
    @staticmethod
    def poisk_s(r):
        return 3.14 * r**2

r = 52
ploschad = Circle.poisk_s(r)
print(f"Площадь круга равна: {ploschad}")