from Items import *

items_in_shop = []
dictionary_items_shop = {}


class Shop:
    def __init__(self):
        self.__opc_menu = 0
        self.__count_buy = 0

    def get_count_buy(self):
        return self.__count_buy

    def set_count_buy(self, count):
        self.__count_buy = count

    def get_opc_menu(self):
        return self.__opc_menu

    def set_opc_menu(self, opc):
        self.__opc_menu = opc

    def add_item_to_shop(self):
        item_balmung = Balmung(BALMUNG)
        item_balmung.set_necessary_strength(BALMUNG_NECESSARY_STRENGTH)
        item_balmung.set_necessary_agility(BALMUNG_NECESSARY_AGILITY)
        item_balmung.set_necessary_vitality(BALMUNG_NECESSARY_VITALITY)
        item_balmung.set_breed(BREED_DWARF)
        item_balmung.set_damage(DAMAGE_BALMUNG)
        item_balmung.set_sell(10000)
        item_balmung.set_buy(50000)
        items_in_shop.append(item_balmung)
        item_ashbringer = Ashbringer(ASHBRINGER)
        item_ashbringer.set_necessary_strength(ASHBRINGER_NECESSARY_STRENGTH)
        item_ashbringer.set_necessary_agility(ASHBRINGER_NECESSARY_AGILITY)
        item_ashbringer.set_necessary_vitality(ASHBRINGER_NECESSARY_VITALITY)
        item_ashbringer.set_breed(BREED_ELF)
        item_ashbringer.set_damage(DAMAGE_ASHBRINGER)
        item_ashbringer.set_sell(10000)
        item_ashbringer.set_buy(50000)
        items_in_shop.append(item_ashbringer)
        item_orb_hell_fire = Orb_hell_fire(ORB_HELL_FIRE)
        item_orb_hell_fire.set_necessary_strength(ORB_HELL_FIRE_NECESSARY_STRENGTH)
        item_orb_hell_fire.set_necessary_agility(ORB_HELL_FIRE_NECESSARY_AGILITY)
        item_orb_hell_fire.set_necessary_vitality(ORB_HELL_FIRE_NECESSARY_VITALITY)
        item_orb_hell_fire.set_breed(BREED_WIZARD)
        item_orb_hell_fire.set_damage(DAMAGE_ORB_HELL_FIRE)
        item_orb_hell_fire.set_sell(10000)
        item_orb_hell_fire.set_buy(50000)
        items_in_shop.append(item_orb_hell_fire)

    def view_items_in_shop_to_buy(self):
        count = 1
        for item in items_in_shop:
            print(
                f"{count}) {item.get_name()} ({item.get_breed()}) [+{item.get_damage()} daño] [{item.get_buy()} {MONEYS}]")
            dictionary_items_shop[count] = item
            count += 1

    def view_items_in_shop_to_sell(self):
        count = 1
        for item in inventory:
            print(
                f"{count}) {item.get_name()} ({item.get_breed()}) [+{item.get_damage()} daño] [{item.get_sell()} {MONEYS}]")
            dictionary[count] = item
            count += 1

    def buy_items(self, character_selected):
        if len(items_in_shop) > 0:
            self.view_items_in_shop_to_buy()
            len_dictionary_items_shop = len(dictionary_items_shop)
            number_item = int(input(NUMBER_ITEM_INPUT))
            if 0 < number_item <= len_dictionary_items_shop:
                if dictionary_items_shop[number_item] is not None:
                    if character_selected.get_money() >= dictionary_items_shop[number_item].get_buy():
                        character_selected.set_money(
                            character_selected.get_money() - dictionary_items_shop[number_item].get_buy())
                        inventory.append(dictionary_items_shop[number_item])
                        self.view_items_in_shop_to_sell()
                        items_in_shop.pop(number_item - 1)
                        print(ITEM_HAS_BEEN_SOLD.format(dictionary_items_shop[number_item].get_name(),
                                                        character_selected.get_money()))
                        dictionary_items_shop[len_dictionary_items_shop - self.get_count_buy()] = None
                        self.set_count_buy(self.get_count_buy() + 1)
                    else:
                        print(NO_MONEY_CHARACTER_SELECTED)
                else:
                    print(ERROR_NO_ITEM_WHICH_THIS_NUMBER)
            else:
                print(ERROR_NO_ITEM_WHICH_THIS_NUMBER)
        else:
            print(NO_ITEMS_IN_SHOP)

    def sell_items(self, character_selected):
        count = 0
        len_dictionary = len(dictionary)
        for i in range(len(inventory)):
            if inventory[i].get_name() == SHORT_SWORD:
                count += 1
            elif inventory[i].get_name() == SHORT_BOW:
                count += 1
            elif inventory[i].get_name() == WALKING_STICK:
                count += 1
        if count == len(inventory):
            print(THE_ITEM_IS_EARLY)
        else:
            self.view_items_in_shop_to_sell()
            number_item = int(input(NUMBER_ITEM_INPUT))
            if 0 < number_item <= len_dictionary - 1:
                if dictionary[number_item].get_name() != SHORT_SWORD \
                        and dictionary[number_item].get_name() != SHORT_BOW \
                        and dictionary[number_item].get_name() != WALKING_STICK:
                    character_selected.set_money(character_selected.get_money() + dictionary[number_item].get_sell())
                    inventory.pop(number_item - 1)
                    dictionary.pop(number_item - 1)
                    print(ITEM_HAS_BEEN_SELL.format(dictionary[number_item].get_name(), character_selected.get_money()))
                else:
                    print(THE_ITEM_IS_EARLY)
            else:
                print(ERROR_NO_ITEM_WHICH_THIS_NUMBER)
