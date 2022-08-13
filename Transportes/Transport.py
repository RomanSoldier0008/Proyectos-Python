cars = []
bikes = []
class Transport:
    def __init__(self, anno, marca, modelo):
        self.anno = anno
        self.marca = marca
        self.modelo = modelo

class Car(Transport):
    def __init__(self, anno, marca, modelo, ruedas, puertas):
        super().__init__(anno, marca, modelo)
        self.ruedas = ruedas
        self.puertas = puertas

    def load_car(self):
        car = Car(self.anno, self.marca, self.modelo, self.ruedas, self.puertas)
        cars.append(car)

    def __str__(self):
        for i in range(len(cars)):
            print("AUTOS\nAÑO: {}\nMARCA: {}\nMODELO: {}\nRUEDAS: {}\nPUERTAS: {}".format(
                cars[i].anno,
                cars[i].marca,
                cars[i].modelo,
                cars[i].ruedas,
                cars[i].puertas))


class Bike(Transport):
    def __init__(self, anno, marca, modelo, ruedas, color):
        super().__init__(anno, marca, modelo)
        self.ruedas = ruedas
        self.color = color

    def load_bike(self):
        bike = Bike(self.anno, self.marca, self.modelo, self.ruedas, self.color)
        bikes.append(bike)

    def __str__(self):
        for i in range(len(bikes)):
            print("BICICLETA\nAÑO: {}\nMARCA: {}\nMODELO: {}\nRUEDAS: {}\nCOLOR: {}".format(
                bikes[i].anno,
                bikes[i].marca,
                bikes[i].modelo,
                bikes[i].ruedas,
                bikes[i].color))
