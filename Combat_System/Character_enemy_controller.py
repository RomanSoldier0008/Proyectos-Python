from Constantes import *

enemies = []

class Character_enemy_controller:
    def __init__(self, character_enemy):
        self.character_enemy = character_enemy

    def add_enemy(self):
        enemies.append(self.character_enemy)

    def search_enemy(self):
        count = 1
        if len(enemies) > 0:
            for i in enemies:
                if count == 1:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(ONE_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count += 1
                elif count == 2:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(TWO_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count += 1
                elif count == 3:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(THREE_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count += 1
                elif count == 4:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(FOUR_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count += 1
                elif count == 5:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(FIVE_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count += 1
                elif count == 6:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(SIX_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count += 1
                elif count == 7:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(SEVEN_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count += 1
                elif count == 8:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(EIGHT_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count += 1
                elif count == 9:
                    print("""
--------------------------------------------
{}
Raza: {}
Nombre: {}
Edad: {}
Fuerza: {}
Agilidad: {}
Vitalidad: {}
--------------------------------------------""".format(NINE_ENEMY,
                                                       i.breed, i.name,
                                                       i.age, i.strength,
                                                       i.agility,i.vitality))
                    count = 10

                else:
                    total = len(enemies)
                    restantes = total - 9
                    if count == total:
                        print(f"Y {restantes} {ENEMY} más...")
                    else:
                        count += 1
        else:
            print(ERROR_NOTHING_CHARACTER_ENEMY)