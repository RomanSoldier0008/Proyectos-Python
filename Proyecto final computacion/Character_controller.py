from Character import *
characters_list = []

class Character_controller:
    def __init__(self, character):
        self.__character = character

    def get_character(self):
        return self.__character

    def set_character(self, character):
        self.__character = character

    def character_add(self):
        if len(characters_list) <= 3:
            characters_list.append(self.get_character())
        else:
            print(ERROR_IN_ADD_CHARACTER_TO_LIST)

    def delete_character(self):
        names_characters = []
        count = len(characters_list) - 1
        if (len(characters_list)) > 0:
            for character in characters_list:
                names_characters.append(character.get_name())
            delete_character = str(
                input(DELETE_CHARACTER_OF_LIST_NAME_INPUT.format(names_characters))).strip().lower().capitalize()
            while True:
                if delete_character == characters_list[count].get_name():
                    characters_list.pop(count)
                    print(HERO_HAS_BEEN_DELETE)
                    break
                else:
                    count -= 1
                    if count < 0:
                        print(ERROR_IN_DELETE_HERO)
                        break
                    else:
                        continue
        else:
            print(ERROR_NO_HEROS)

    def assign_breed_and_name(self):
        if len(characters_list) <= MAX_LIMIT_CREATE_CHARACTER:
            while True:
                breed = str(input(CHARACTER_HERO_INPUT)).strip().lower().capitalize()
                if breed == BREED_ELF or breed == BREED_WIZARD or breed == BREED_DWARF:
                    break
                else:
                    print(ERROR_IN_BREED_HERO)
            name = str(input(CHARACTER_NAME_HERO_INPUT)).strip().lower().capitalize()
            self.attribute_hero(breed, name)
        else:
            print(ERROR_MAX_LIMIT_CREATE_CHARACTER)

    def attribute_hero(self, breed, name):
        while True:
            print(REMAINDER.format(MAX_ATTRIBUTE_HERO))
            strength = int(input(STRENGTH_HERO_INPUT))
            rest = MAX_ATTRIBUTE_HERO - strength
            print(REMAINDER.format(rest))
            agility = int(input(AGILITY_HERO_INPUT))
            rest -= agility
            print(REMAINDER.format(rest))
            vitality = int(input(VITALITY_HERO_INPUT))
            if (strength + agility + vitality) == MAX_ATTRIBUTE_HERO \
                    and strength > 0 \
                    and agility > 0 \
                    and vitality > 0:
                break
            else:
                print(ERROR_IN_POINTS_HERO)
        self.choose_hero(breed, name, strength, agility, vitality)

    def choose_hero(self, breed, name, strength, agility, vitality):
        if breed == BREED_ELF:
            character_hero = Elf(breed, name, strength, agility, vitality, EXP_STARTED, LEVEL_STARTED)
            character_hero.add_power_elf(POWER_START_ELF)
        elif breed == BREED_WIZARD:
            character_hero = Wizard(breed, name, strength, agility, vitality, EXP_STARTED, LEVEL_STARTED)
            character_hero.add_power_wizard(POWER_START_WIZARD)
        elif breed == BREED_DWARF:
            character_hero = Dwarf(breed, name, strength, agility, vitality, EXP_STARTED, LEVEL_STARTED)
            character_hero.add_power_dwarf(POWER_START_DWARF)

        self.set_character(character_hero)
        self.character_add()