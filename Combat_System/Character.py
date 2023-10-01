from Constantes import *

class Character:
    def __init__(self, breed, name, age, strength, agility, vitality):
        self.breed = breed
        self.name = name
        self.age = age
        self.strength = strength
        self.agility = agility
        self.vitality = vitality

class Elf(Character):
    def __init__(self, breed, name, age, strength, agility, vitality):
        super().__init__(breed, name, age, strength, agility, vitality)

    def add_atribute_power_up(self):
        self.agility += 2

    def __str__(self):
        if self.name != NAME_ENEMY_ELF:
            return """
--------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------""".format(HERO, self.breed, self.name, self.age, self.strength, self.agility, self.vitality)

        elif self.name == NAME_ENEMY_ELF:
            return """
--------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------""".format(ENEMY, self.breed, self.name, self.age, self.strength, self.agility, self.vitality)


class Wizard(Character):
    def __init__(self, breed, name, age, strength, agility, vitality):
        super().__init__(breed, name, age, strength, agility, vitality)

    def add_atribute_power_up(self):
        self.vitality += 2

    def __str__(self):
        if self.name != NAME_ENEMY_WIZARD:
            return """
--------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------""".format(HERO, self.breed, self.name, self.age, self.strength, self.agility, self.vitality)

        elif self.name == NAME_ENEMY_WIZARD:
            return """
--------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------""".format(ENEMY,self.breed, self.name, self.age, self.strength, self.agility, self.vitality)

class Dwarf(Character):
    def __init__(self, breed, name, age, strength, agility, vitality):
        super().__init__(breed, name, age, strength, agility, vitality)

    def add_atribute_power_up(self):
        self.strength += 2

    def __str__(self):
        if self.name != NAME_ENEMY_DWARF:
            return """
--------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------""".format(HERO, self.breed, self.name, self.age, self.strength, self.agility, self.vitality)

        elif self.name == NAME_ENEMY_DWARF:
            return """
--------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------""".format(ENEMY, self.breed, self.name, self.age, self.strength, self.agility, self.vitality)