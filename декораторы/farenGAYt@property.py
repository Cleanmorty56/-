class Temperature:
    def __init__(self, celsiuuu):
        self.celsiuuu = celsiuuu

    @property
    def farengayt(self):
        return self.celsiuuu * 9/5 + 32


fareng = Temperature(11.11111111112)
print(f"Температура в градусах Фаренгейта: {fareng.farengayt}")