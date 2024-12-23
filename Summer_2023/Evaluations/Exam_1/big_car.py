from car import Car


class BigCar(Car):

    def __init__(self, steel_unit=2, rubber_unit=1):
        super().__init__(steel_unit, rubber_unit)

    def __str__(self) -> str:
        return f"Je suis une auto de grande taille, je consomme {self.steel_unit} unité(s) d'acier " \
               f"et {self.rubber_unit} unité(s) de caoutchouc"
