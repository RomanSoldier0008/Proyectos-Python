from Game import *

characters_hero = []
names = []

select_is = "no"


class Character_hero_controller:
    def __init__(self, character_hero):
        self.character_hero = character_hero

    def add_hero_to(self):
        if 0 == len(characters_hero):
            characters_hero.append(self.character_hero)
        elif 0 < len(characters_hero) < 3:
            for i in characters_hero:
                if i.name != self.character_hero.name:
                    characters_hero.append(self.character_hero)
                    break
                else:
                    print(ERROR_NAME_ALREDY_EXIST)
                    break
        else:
            print(ERROR_MAX_LIMIT_CREATE_CHARACTER)

    def search_hero(self):
        for i in range(len(characters_hero)):
            if characters_hero[i].vitality <= 0:
                characters_hero.pop(i)
        count = 1
        if len(characters_hero) > 0:
            for character in characters_hero:
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
--------------------------------------------""".format(ONE_HERO,
                                                       character.breed, character.name,
                                                       character.age, character.strength,
                                                       character.agility, character.vitality))
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
--------------------------------------------""".format(TWO_HERO,
                                                       character.breed, character.name,
                                                       character.age, character.strength,
                                                       character.agility, character.vitality))
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
--------------------------------------------""".format(THREE_HERO,
                                                       character.breed, character.name,
                                                       character.age, character.strength,
                                                       character.agility, character.vitality))
        else:
            print(ERROR_NOTHING_CHARACTER_HERO)

    def character_select(self):
        for i in range(len(characters_hero)):
            if characters_hero[i].vitality <= 0:
                characters_hero.pop(i)
                names.pop(i)
        global select_character_in_game, select_is
        count = 0
        found = "no"
        if len(characters_hero) > 0:
            for character in characters_hero:
                names.append(character.name)
                name_counter = names.count(character.name)
                if name_counter > 1:
                    index = names.index(character.name)
                    names.pop(index)
            print(OPTION_SELECT_CHARACTER, names)
            character_name = str(input(NAME_INPUT_SELECT_CHARACTER)).strip().lower().capitalize()
            for i in characters_hero:
                count += 1
                if character_name in i.name:
                    select_is = "si"
                    select_character_in_game = i
                    print(select_character_in_game)
                    found = "si"
                if count == len(characters_hero) and found == "no":
                    print(ERROR_NO_NAME_CHARACTER_EXIST)
        else:
            print(ERROR_NOTHING_CHARACTER_HERO)

    def start_game(self):
        if len(characters_hero) <= 0 or len(enemies) <= 0 or select_is == "no":
            print(ERROR_NOTHING_CHARACTER_HERO_AND_ENEMY)
        else:
            Game(select_character_in_game, enemies).game_start()