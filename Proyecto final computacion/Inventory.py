from Character_controller import *
from constant import *

inventory = []
dictionary = {}

class Inventory:
    def __init__(self):
        self.__opc = 0

    def get_opc(self):
        return self.__opc

    def set_opc(self, opc):
        self.__opc = opc

    def add_item_to_inventory(self, item):
        inventory.append(item)

    def view_inventory(self):
        count = 1
        for item in inventory:
            print(f"{count}) {item.get_name()} ({item.get_breed()}) [+{item.get_damage()} daño]")
            dictionary[count] = item
            count += 1

    def select_item_to_hand(self, character_selected):
        len_inventory = len(inventory)
        if len(inventory) > 0:
            self.view_inventory()
            number_item = int(input(NUMBER_ITEM_INPUT))
            if 0 < number_item <= len_inventory:
                if character_selected.get_breed() == dictionary[number_item].get_breed():
                    if character_selected.get_strength() >= inventory[number_item - 1].get_necessary_strength() and \
                            character_selected.get_agility() >= inventory[number_item - 1].get_necessary_agility() and \
                            character_selected.get_vitality() >= inventory[number_item - 1].get_necessary_vitality():
                        character_selected.set_primary_hand(dictionary[number_item])
                    else:
                        print(POINTS_REST)
                        you_lack_strength = inventory[number_item - 1].get_necessary_strength() - character_selected.get_strength()
                        you_lack_agility = inventory[number_item - 1].get_necessary_agility() - character_selected.get_agility()
                        you_lack_vitality = inventory[number_item - 1].get_necessary_vitality() - character_selected.get_vitality()
                        if you_lack_strength > 0:
                            print(YOU_LACK_S.format(you_lack_strength))
                        if you_lack_agility > 0:
                            print(YOU_LACK_A.format(you_lack_agility))
                        if you_lack_vitality > 0:
                            print(YOU_LACK_V.format(you_lack_vitality))
                else:
                    print(ITEM_BY_OTHER_BREED.format(dictionary[number_item].get_breed()))
            else:
                print(ERROR_NO_ITEM_WHICH_THIS_NUMBER)
        else:
            print(NO_ITEM_IN_INVENTORY)

    def early_item(self):
        for item in inventory:
            if item.get_name() == SHORT_BOW:
                for character in characters_list:
                    if character.get_breed() == BREED_ELF:
                        character.set_primary_hand(item)
            elif item.get_name() == SHORT_SWORD:
                for character in characters_list:
                    if character.get_breed() == BREED_DWARF:
                        character.set_primary_hand(item)
            elif item.get_name() == WALKING_STICK:
                for character in characters_list:
                    if character.get_breed() == BREED_WIZARD:
                        character.set_primary_hand(item)

    def delete_early_items(self):
        count_short_sword = 0
        count_short_bow = 0
        count_walking_stick = 0
        for item in inventory:
            if item.get_name() == SHORT_SWORD:
                count_short_sword += 1
            elif item.get_name() == SHORT_BOW:
                count_short_bow += 1
            elif item.get_name() == WALKING_STICK:
                count_walking_stick += 1
        count = len(inventory) - 1
        while count != 0:
            if count_short_sword > 1 and inventory[count].get_name() == SHORT_SWORD:
                inventory.pop(count)
                count_short_sword -= 1
            elif count_short_bow > 1 and inventory[count].get_name() == SHORT_BOW:
                inventory.pop(count)
                count_short_bow -= 1
            elif count_walking_stick > 1 and inventory[count].get_name() == WALKING_STICK:
                inventory.pop(count)
                count_walking_stick -= 1
            count -= 1