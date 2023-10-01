from random import randint
from Inventory import *

drop_percentage_weapons = [1, 2, 2, 2, 2, 1, 2, 2, 2, 2]
drop_percentage_money = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2]

class Items:
    def __init__(self, name=None):
        self.__name = name
        self.__price_to_buy = 0
        self.__sell = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_buy(self):
        return self.__price_to_buy

    def set_buy(self, price):
        self.__price_to_buy = price

    def get_sell(self):
        return self.__sell

    def set_sell(self, price):
        self.__sell = price

class Money(Items):
    def __init__(self, name):
        super().__init__(name)

    def drop_money_items(self, character, enemy, difficult):
        random_number_drop_percentage = randint(0, 9)
        if drop_percentage_money[random_number_drop_percentage] == 1:
            if difficult == DIFFICULT_EASY:

                character.set_money((character.get_money() + (MONEY_TO_DROP * BONUS_MONEY_DIFFICULT_EASY * (enemy[0].get_strength() + enemy[0].get_agility()))))
                money = MONEY_TO_DROP * (BONUS_MONEY_DIFFICULT_EASY * (enemy[0].get_strength() + enemy[0].get_agility()))
            elif difficult == DIFFICULT_NORMAL:

                character.set_money((character.get_money() + (MONEY_TO_DROP * BONUS_MONEY_DIFFICULT_NORMAL * (enemy[0].get_strength() + enemy[0].get_agility()))))
                money = MONEY_TO_DROP * (BONUS_MONEY_DIFFICULT_NORMAL * (enemy[0].get_strength() + enemy[0].get_agility()))
            elif difficult == DIFFICULT_HARD:

                character.set_money((character.get_money() + (MONEY_TO_DROP * BONUS_MONEY_DIFFICULT_HARD * (enemy[0].get_strength() + enemy[0].get_agility()))))
                money = MONEY_TO_DROP * (BONUS_MONEY_DIFFICULT_HARD * (enemy[0].get_strength() + enemy[0].get_agility()))
            print(MONEY_HAS_BEEN_DROP.format(money))
        else:
            print(MONEY_HAS_NOT_BEEN_DROP)

class Weapon(Items):
    def __init__(self, name):
        self.__necessary_strength = SHORT_SWORD_NECESSARY_STRENGTH
        self.__necessary_agility = SHORT_SWORD_NECESSARY_AGILITY
        self.__necessary_vitality = SHORT_SWORD_NECESSARY_VITALITY
        self.__damage = DAMAGE_SHORT_SWORD
        self.__breed = BREED_DWARF
        super().__init__(name)

    def drop_weapon_items(self):
        random_number_drop_percentage = randint(0, 9)
        random_number_item_drop = randint(0, 5)
        if drop_percentage_weapons[random_number_drop_percentage] == 1:
            if random_number_item_drop == 0:
                item = War_axe(WAR_AXE)
                item.set_necessary_vitality(WAR_AXE_NECESSARY_STRENGTH)
                item.set_necessary_vitality(WAR_AXE_NECESSARY_AGILITY)
                item.set_necessary_vitality(WAR_AXE_NECESSARY_VITALITY)
                item.set_breed(BREED_DWARF)
                item.set_damage(DAMAGE_WAR_AXE)
            elif random_number_item_drop == 1:
                item = Doom_hammer(DOOM_HAMMER)
                item.set_necessary_vitality(DOOM_HAMMER_NECESSARY_STRENGTH)
                item.set_necessary_vitality(DOOM_HAMMER_NECESSARY_AGILITY)
                item.set_necessary_vitality(DOOM_HAMMER_NECESSARY_VITALITY)
                item.set_breed(BREED_DWARF)
                item.set_damage(DAMAGE_DOOM_HAMMER)
            elif random_number_item_drop == 2:
                item = Luna_bow(LUNA_BOW)
                item.set_necessary_strength(LUNA_BOW_NECESSARY_STRENGTH)
                item.set_necessary_agility(LUNA_BOW_NECESSARY_AGILITY)
                item.set_necessary_vitality(LUNA_BOW_NECESSARY_VITALITY)
                item.set_breed(BREED_ELF)
                item.set_damage(DAMAGE_LUNA_BOW)
            elif random_number_item_drop == 3:
                item = Lux_bow(LUX_BOW)
                item.set_necessary_strength(LUX_BOW_NECESSARY_STRENGTH)
                item.set_necessary_agility(LUX_BOW_NECESSARY_AGILITY)
                item.set_necessary_vitality(LUX_BOW_NECESSARY_VITALITY)
                item.set_breed(BREED_ELF)
                item.set_damage(DAMAGE_LUX_BOW)
            elif random_number_item_drop == 4:
                item = Soul_calibur(SOUL_CALIBUR)
                item.set_necessary_strength(SOUL_CALIBUR_NECESSARY_STRENGTH)
                item.set_necessary_agility(SOUL_CALIBUR_NECESSARY_AGILITY)
                item.set_necessary_vitality(SOUL_CALIBUR_NECESSARY_VITALITY)
                item.set_breed(BREED_WIZARD)
                item.set_damage(DAMAGE_SOUL_CALIBUR)
            elif random_number_item_drop == 5:
                item = Staff_of_pure_goodness(STAFF_OF_PURE_GOODNESS)
                item.set_necessary_strength(STAFF_OF_PURE_GOODNESS_NECESSARY_STRENGTH)
                item.set_necessary_agility(STAFF_OF_PURE_GOODNESS_NECESSARY_AGILITY)
                item.set_necessary_vitality(STAFF_OF_PURE_GOODNESS_NECESSARY_VITALITY)
                item.set_breed(BREED_WIZARD)
                item.set_damage(DAMAGE_STAFF_OF_PURE_GOODNESS)
            item.set_buy(10000)
            item.set_sell(3000)
            Inventory().add_item_to_inventory(item)
            print(ITEM_ADDED_TO_INVENTORY.format(item.get_name()))
        else:
            print(NO_DROP_ITEM)

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage = damage

    def get_necessary_strength(self):
        return self.__necessary_strength

    def set_necessary_strength(self, strength):
        self.__necessary_strength = strength

    def get_necessary_agility(self):
        return self.__necessary_agility

    def set_necessary_agility(self, agility):
        self.__necessary_agility = agility

    def get_necessary_vitality(self):
        return self.__necessary_vitality

    def set_necessary_vitality(self, vitality):
        self.__necessary_agility = vitality

# ARMAS ENANO

class Short_sword(Weapon):
    def __init__(self, name):
        super().__init__(name)

class War_axe(Weapon):
    def __init__(self, name):
        super().__init__(name)

class Doom_hammer(Weapon):
    def __init__(self, name):
        super().__init__(name)

# ARMAS ELFO
class Short_bow(Weapon):
    def __init__(self, name):
        super().__init__(name)

class Luna_bow(Weapon):
    def __init__(self, name):
        super().__init__(name)

class Lux_bow(Weapon):
    def __init__(self, name):
        super().__init__(name)

# ARMAS MAGO
class Walking_stick(Weapon):
    def __init__(self, name):
        super().__init__(name)

class Soul_calibur(Weapon):
    def __init__(self, name):
        super().__init__(name)

class Staff_of_pure_goodness(Weapon):
    def __init__(self, name):
        super().__init__(name)

# ARMAS TIENDA
    # ENANO
class Balmung(Weapon):
    def __init__(self, name):
        super().__init__(name)

    # ELFO
class Ashbringer(Weapon):
    def __init__(self, name):
        super().__init__(name)

    # MAGO
class Orb_hell_fire(Weapon):
    def __init__(self, name):
        super().__init__(name)