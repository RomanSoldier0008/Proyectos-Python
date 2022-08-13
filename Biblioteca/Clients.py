from Constants import *
class Clients:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def __str__(self):
        return RETURN_CLIENTS_FORMAT.format(self.nombre, self.edad, self.direccion)