class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def ploschad(self):
        return self.width * self.height


pryamougol = Rectangle(23, 3)
print(pryamougol.ploschad)