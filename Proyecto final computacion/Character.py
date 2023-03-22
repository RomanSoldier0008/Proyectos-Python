from constant import *

class Character:
    def __init__(self, breed, name, strength, agility, vitality, exp, level):
        self.__breed = breed
        self.__name = name
        self.__strength = strength
        self.__agility = agility
        self.__vitality = vitality
        self.__exp = exp
        self.__level = level
        self.__exp_to_level_up = CONSTANT_EXP_GOAL
        self.__primary_hand = None
        self.__money = 0

    def __str__(self):
        return RETURN_HERO_FORMAT.format(HERO,
                                         self.get_breed(),
                                         self.get_name(),
                                         self.get_strength(),
                                         self.get_agility(),
                                         self.get_vitality(),
                                         self.get_exp(),
                                         self.get_level())

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_primary_hand(self):
        return self.__primary_hand

    def set_primary_hand(self, item):
        self.__primary_hand = item

    def get_exp_to_level_up(self):
        return self.__exp_to_level_up

    def set_exp_to_level_up(self, count):
        self.__exp_to_level_up = count

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_strength(self):
        return self.__strength

    def set_strength(self, strength):
        self.__strength = strength

    def get_agility(self):
        return self.__agility

    def set_agility(self, agility):
        self.__agility = agility

    def get_vitality(self):
        return self.__vitality

    def set_vitality(self, vitality):
        self.__vitality = vitality

    def get_exp(self):
        return self.__exp

    def set_exp(self, exp):
        self.__exp = exp

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level


class Elf(Character):
    def __init__(self, __breed, __name, __strenght, __agility, __vitality, __exp, __level):
        super().__init__(__breed, __name, __strenght, __agility, __vitality, __exp, __level)

    def add_power_elf(self, power):
        new_agility = super().get_agility() + power
        super().set_agility(new_agility)


class Wizard(Character):
    def __init__(self, __breed, __name, __strenght, __agility, __vitality, __exp, __level):
        super().__init__(__breed, __name, __strenght, __agility, __vitality, __exp, __level)

    def add_power_wizard(self, power):
        new_vitality = super().get_vitality() + power
        super().set_vitality(new_vitality)


class Dwarf(Character):
    def __init__(self, __breed, __name, __strenght, __agility, __vitality, __exp, __level):
        super().__init__(__breed, __name, __strenght, __agility, __vitality, __exp, __level)

    def add_power_dwarf(self, power):
        new_strength = super().get_strength() + power
        super().set_strength(new_strength)