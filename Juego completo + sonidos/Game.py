from Enemies import *
from time import sleep
from Shop import *
import pygame

pygame.init()

damages = (0, 0, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4)
enemies = []


class Game:
    def __init__(self, difficult, characters_list):
        self.__difficult = difficult
        self.characters_list = characters_list
        self.__enemies_shot_down = 0
        self.__turn = 0
        self.__character_selected = None
        self.__exit = False
        self.__option_menu = 0
        self.__option_menu_play = 0
        self.__time_music = 0
        self.__start_music = "si"
        self.__first_time = True
        self.__dice_enemy = 0
        self.__damage_enemy = 0
        self.__total_damage_enemy = 0
        self.__dice_player = 0
        self.__damage_player = 0
        self.__total_damage_player = 0
        self.__first_enemy_vitality = 0

    def get_first_enemy_vitality(self):
        return self.__first_enemy_vitality

    def set_first_enemy_vitality(self, vitality):
        self.__first_enemy_vitality = vitality

    def get_damage_player(self):
        return self.__damage_player

    def set_damage_player(self, damage):
        self.__damage_player = damage

    def get_total_damage_player(self):
        return self.__total_damage_player

    def set_total_damage_player(self, total):
        self.__total_damage_player = total

    def get_dice_player(self):
        return self.__dice_player

    def set_dice_player(self, dice):
        self.__dice_player = dice

    def get_total_damage_enemy(self):
        return self.__total_damage_enemy

    def set_total_damage_enemy(self, total_damage):
        self.__total_damage_enemy = total_damage

    def get_damage_enemy(self):
        return self.__damage_enemy

    def set_damage_enemy(self, damage):
        self.__damage_enemy = damage

    def get_dice_enemy(self):
        return self.__dice_enemy

    def set_dice_enemy(self, dice):
        self.__dice_enemy = dice

    def get_first_time(self):
        return self.__first_time

    def set_first_time(self, boolean):
        self.__first_time = boolean

    def get_start_music(self):
        return self.__start_music

    def set_start_music(self, start):
        self.__start_music = start

    def get_time_music(self):
        return self.__time_music

    def set_time_music(self, time):
        self.__time_music = time

    def get_option_menu_play(self):
        return self.__option_menu_play

    def set_option_menu_play(self, option):
        self.__option_menu_play = option

    def get_option_menu(self):
        return self.__option_menu

    def set_option_menu(self, option):
        self.__option_menu = option

    def get_exit(self):
        return self.__exit

    def set_exit(self, back):
        self.__exit = back

    def get_character_selected(self):
        return self.__character_selected

    def set_character_selected(self, character_selected):
        self.__character_selected = character_selected

    def get_difficult(self):
        return self.__difficult

    def set_difficult(self, difficult):
        self.__difficult = difficult

    def get_enemies_shot_down(self):
        return self.__enemies_shot_down

    def set_enemies_shot_down(self, enemies_shot_down):
        self.__enemies_shot_down = enemies_shot_down

    def get_turn(self):
        return self.__turn

    def set_turn(self, turn):
        self.__turn = turn

    def listen_music_sword(self):
        pygame.mixer.music.fadeout(4000)
        pygame.mixer.music.load('Sounds/Menu_espada.mp3')
        pygame.mixer.music.play(-1)

    def listen_sound_make_dispute(self):
        pygame.mixer.music.load('Sounds/Hacer_disputa.mp3')
        pygame.mixer.music.play(1)

    def listen_music_play(self):
        pygame.mixer.music.load('Sounds/Menu_jugar.mp3')
        if self.get_time_music() > 0:
            pygame.mixer.music.play(-1, self.get_time_music())
        else:
            pygame.mixer.music.play(-1)

    def listen_sound_victory(self):
        pygame.mixer.music.fadeout(2000)
        pygame.mixer.music.load('Sounds/Victoria.mp3')
        pygame.mixer.music.play(1)

    def listen_sound_defeat(self):
        pygame.mixer.music.fadeout(2000)
        pygame.mixer.music.load('Sounds/Derrota.mp3')
        pygame.mixer.music.play(1)

    def menu(self):
        while not self.get_exit():
            if self.get_option_menu() != "2" and self.get_start_music() == "si":
                self.listen_music_sword()
            self.set_option_menu(str(input(
                MENU_GAME_INPUT.format(self.get_difficult(), len(self.characters_list),
                                       (drop_percentage_weapons.count(1) / len(drop_percentage_weapons) * 100),
                                       (drop_percentage_money.count(1) / len(drop_percentage_money)) * 100))))
            if self.get_option_menu() == "1":
                if self.get_difficult() != "Ninguna":
                    self.set_turn(0)
                    self.start()
                    self.set_start_music("si")
                else:
                    self.set_start_music("no")
                    print(ERROR_START_NO_DIFFICULT)

            elif self.get_option_menu() == "2":
                self.delete_enemies()
                self.choose_difficult()

            elif self.get_option_menu() == "3":
                self.set_exit(True)

            else:
                print(ERROR_IN_OPC_MENU)

    def delete_enemies(self):
        i = len(enemies) - 1
        while len(enemies) != 0:
            enemies.pop(i)
            i -= 1

    def choose_difficult(self):
        while True:
            difficult = str(input(DIFFICULT_INPUT)).strip().lower().capitalize()
            if difficult == DIFFICULT_EASY or \
                    difficult == DIFFICULT_NORMAL or \
                    difficult == DIFFICULT_HARD:
                self.set_difficult(difficult)
                self.generate_enemies()
                break
            else:
                print(ERROR_IN_SELECTION_DIFFICULT)

    def generate_enemies(self):
        for enemy in range(0, (NUMBER_OF_ENEMIES - self.get_enemies_shot_down())):
            if self.get_difficult() == DIFFICULT_EASY:
                random_attribute_strength = randint(MIN_RANDOM_ATTRIBUTE_ENEMY_EASY, MAX_RANDOM_ATTRIBUTE_ENEMY_EASY, )
                excess = MAX_ATTRIBUTE_ENEMY_EASY - random_attribute_strength
                random_attribute_agility = randint(MIN_RANDOM_ATTRIBUTE_ENEMY_EASY, MAX_RANDOM_ATTRIBUTE_ENEMY_EASY)
                total_excess = excess - random_attribute_agility
                random_attribute_vitality = total_excess + SUM_VITALITY_ENEMY_EASY
            elif self.get_difficult() == DIFFICULT_NORMAL:
                random_attribute_strength = randint(MIN_RANDOM_ATTRIBUTE_ENEMY_NORMAL,
                                                    MAX_RANDOM_ATTRIBUTE_ENEMY_NORMAL)
                excess = MAX_ATTRIBUTE_ENEMY_NORMAL - random_attribute_strength
                random_attribute_agility = randint(MIN_RANDOM_ATTRIBUTE_ENEMY_NORMAL, MAX_RANDOM_ATTRIBUTE_ENEMY_NORMAL)
                total_excess = excess - random_attribute_agility
                random_attribute_vitality = total_excess + SUM_VITALITY_ENEMY_NORMAL
            elif self.get_difficult() == DIFFICULT_HARD:
                random_attribute_strength = randint(MIN_RANDOM_ATTRIBUTE_ENEMY_HARD, MAX_RANDOM_ATTRIBUTE_ENEMY_HARD)
                excess = MAX_ATTRIBUTE_ENEMY_HARD - random_attribute_strength
                random_attribute_agility = randint(MIN_RANDOM_ATTRIBUTE_ENEMY_HARD, MAX_RANDOM_ATTRIBUTE_ENEMY_HARD)
                total_excess = excess - random_attribute_agility
                random_attribute_vitality = total_excess + SUM_VITALITY_ENEMY_HARD
            self.create_enemies(random_attribute_strength, random_attribute_agility, random_attribute_vitality)

    def create_enemies(self, strength, agility, vitality):
        random_enemy = randint(1, 3)
        if random_enemy == 1:
            breed = "Orco"
            character_enemy = Orc(breed, strength, agility, vitality)
            enemies.append(character_enemy)
        elif random_enemy == 2:
            breed = "Troll"
            character_enemy = Orc(breed, strength, agility, vitality)
            enemies.append(character_enemy)
        elif random_enemy == 3:
            breed = "Monstruo"
            character_enemy = Orc(breed, strength, agility, vitality)
            enemies.append(character_enemy)

    def start(self):
        while not self.get_exit():
            if len(self.characters_list) > 0 and self.get_enemies_shot_down() != NUMBER_OF_ENEMIES:
                self.assign_turn()
            if len(self.characters_list) == 0 and self.get_enemies_shot_down() != NUMBER_OF_ENEMIES:
                self.listen_sound_defeat()
                print(GAME_OVER)
                sleep(4)
                self.set_enemies_shot_down(NUMBER_OF_ENEMIES)
                self.set_exit(True)
                break
            elif self.get_enemies_shot_down() == NUMBER_OF_ENEMIES and len(self.characters_list) > 0:
                self.listen_sound_victory()
                print(GAME_WIN)
                sleep(4)
                self.set_exit(True)
                self.set_enemies_shot_down(0)
                break

    def assign_turn(self):
        self.set_turn(self.get_turn() + 1)
        if self.get_turn() % 2 == 0:
            self.turn_enemy()
            self.print()
        else:
            self.select_option_player()

    def print(self):
        if self.get_character_selected().get_vitality() <= 0:
            print(f"{ENEMY_DAMAGE.format(self.get_character_selected().get_name(), self.get_total_damage_enemy())}\n"
                  f"{HERO_DAMAGE.format(self.get_character_selected().get_name(), self.get_total_damage_player())}\n"
                  f"{HERO_DEAD.format(self.get_character_selected().get_name())}")
            self.set_turn(0)
            self.select_hero()
            return
        else:
            print(ENEMY_DAMAGE.format(self.get_character_selected().get_name(), self.get_total_damage_enemy()))

        if self.get_first_enemy_vitality() <= 0 and not self.get_character_selected().get_vitality() <= 0:
            print(f"{HERO_DAMAGE.format(self.get_character_selected().get_name(), self.get_total_damage_player())}")
            Money(MONEYS).drop_money_items(self.get_character_selected(), enemies, self.get_difficult())
            Weapon(SHORT_SWORD).drop_weapon_items()
        else:
            if self.get_character_selected().get_vitality() > 0:
                print(HERO_DAMAGE.format(self.get_character_selected().get_name(), self.get_total_damage_player()))
        sleep(8)

    def turn_enemy(self):
        self.set_dice_enemy(randint(0, 11))
        self.set_damage_enemy(damages[self.get_dice_enemy()])
        self.set_total_damage_enemy(
            (enemies[0].get_strength() // self.get_character_selected().get_agility()) + self.get_damage_enemy())
        self.get_character_selected().set_vitality(
            self.get_character_selected().get_vitality() - self.get_total_damage_enemy())
        if self.get_character_selected().get_vitality() <= 0:
            count = 0
            for character in self.characters_list:
                if character.get_name() == self.get_character_selected().get_name():
                    self.characters_list.pop(count)
                    self.assign_turn()
                count += 1
            sleep(2)

    def turn_player(self, character_selected):
        self.set_dice_player(randint(0, 11))
        self.set_damage_player(damages[self.get_dice_player()] + character_selected.get_primary_hand().get_damage())
        self.set_total_damage_player(
            (character_selected.get_strength() // enemies[0].get_agility()) + self.get_damage_player())
        self.set_first_enemy_vitality(enemies[0].get_vitality() - self.get_total_damage_player())
        enemies[0].set_vitality(enemies[0].get_vitality() - self.get_total_damage_player())
        if enemies[0].get_vitality() <= 0:
            self.set_enemies_shot_down(self.get_enemies_shot_down() + 1)
            self.drop_exp(character_selected)
            enemies.pop(0)

    def select_hero(self):
        if len(self.characters_list) > 0:
            count = 0
            names_characters = []
            while True:
                names_characters.append(self.characters_list[count].get_name())
                if len(names_characters) == len(self.characters_list):
                    character_selected = str(input(SELECT_HERO_TO_ATTACK.format(names_characters))).strip().lower().capitalize()
                    for i in range(len(self.characters_list)):
                        if self.characters_list[i].get_name() == character_selected:
                            character_selected = self.characters_list[i]
                            self.set_character_selected(character_selected)
                            return
                        else:
                            if (len(self.characters_list) - 1) == i:
                                print(ERROR_IN_SELECT_HERO)
                                names_characters = []
                                count = -1
                            else:
                                continue
                count += 1
        else:
            return

    def drop_exp(self, character_selected):
        exp = character_selected.get_exp() + enemies[0].get_strength() * CONSTANT_EXP_EASY

        if self.get_difficult() == DIFFICULT_NORMAL:
            exp = character_selected.get_exp() + enemies[0].get_strength() * CONSTANT_EXP_NORMAL

        elif self.get_difficult() == DIFFICULT_HARD:
            exp = character_selected.get_exp() + enemies[0].get_strength() * CONSTANT_EXP_HARD
        self.level_up(character_selected, exp)

    def level_up(self, character_selected, exp):
        character_selected.set_exp_to_level_up(character_selected.get_level() * CONSTANT_EXP_GOAL)
        character_selected.set_exp(exp)
        while character_selected.get_exp() >= character_selected.get_exp_to_level_up():
            character_selected.set_level(character_selected.get_level() + 1)
            character_selected.set_strength(character_selected.get_strength() + SUM_ATTRIBUTE_WHEN_LEVEL_UP)
            character_selected.set_agility(character_selected.get_agility() + SUM_ATTRIBUTE_WHEN_LEVEL_UP)
            character_selected.set_vitality(character_selected.get_vitality() + SUM_ATTRIBUTE_WHEN_LEVEL_UP)
            character_selected.set_exp_to_level_up((character_selected.get_level() * CONSTANT_EXP_GOAL))
            print(LEVEL_UP.format(character_selected.get_level()))

    def select_option_player(self):
        if self.get_option_menu_play() != 2 and self.get_option_menu_play() != 3 and self.get_option_menu_play() != 4:
            pygame.mixer.music.fadeout(4000)
            self.listen_music_play()

        if self.get_first_time():
            self.select_hero()
            self.early_item()
            shop = Shop()
            shop.add_item_to_shop()
            self.set_first_time(False)

        if self.get_character_selected().get_vitality() > 0:
            self.set_option_menu_play(int(input(SELECT_OPTION_PLAYER_INPUT.format(
                self.get_character_selected().get_name(), enemies[0].get_breed(), enemies[0].get_strength(),
                enemies[0].get_agility(), enemies[0].get_vitality(), len(enemies),
                self.get_character_selected().get_breed(),
                self.get_character_selected().get_primary_hand().get_name(),
                self.get_character_selected().get_strength(),
                self.get_character_selected().get_agility(), self.get_character_selected().get_vitality(),
                self.get_character_selected().get_exp(), self.get_character_selected().get_exp_to_level_up(),
                self.get_character_selected().get_level(), self.get_character_selected().get_money()))))

        self.capture_the_option_player(self.get_option_menu_play())

    def capture_the_option_player(self, option):
        if self.get_character_selected().get_vitality() > 0:
            if option == 1:
                self.set_time_music(pygame.mixer.music.get_pos() / 1000)
                self.listen_sound_make_dispute()
                self.turn_player(self.get_character_selected())

            elif option == 2:
                self.set_time_music(pygame.mixer.music.get_pos() / 1000)
                self.select_hero()
                self.select_option_player()

            elif option == 3:
                self.set_time_music(pygame.mixer.music.get_pos() / 1000)
                self.menu_inventory(self.get_character_selected())
                self.select_option_player()

            elif option == 4:
                self.set_option_menu(0)
                self.set_option_menu_play(0)
                self.set_start_music("si")
                self.menu()

    def early_item(self):
        for character in self.characters_list:
            if character.get_breed() == BREED_DWARF:
                item = Short_sword(SHORT_SWORD)
                item.set_sell(1)
                item.set_buy(1)
                Inventory().add_item_to_inventory(item)
            elif character.get_breed() == BREED_ELF:
                item = Short_bow(SHORT_BOW)
                item.set_necessary_strength(SHORT_BOW_NECESSARY_STRENGTH)
                item.set_necessary_agility(SHORT_BOW_NECESSARY_AGILITY)
                item.set_necessary_vitality(SHORT_BOW_NECESSARY_VITALITY)
                item.set_breed(BREED_ELF)
                item.set_sell(1)
                item.set_buy(1)
                Inventory().add_item_to_inventory(item)
            elif character.get_breed() == BREED_WIZARD:
                item = Walking_stick(WALKING_STICK)
                item.set_necessary_strength(WALKING_STICK_NECESSARY_STRENGTH)
                item.set_necessary_agility(WALKING_STICK_NECESSARY_AGILITY)
                item.set_necessary_vitality(WALKING_STICK_NECESSARY_VITALITY)
                item.set_breed(BREED_WIZARD)
                item.set_sell(1)
                item.set_buy(1)
                Inventory().add_item_to_inventory(item)
        Inventory().delete_early_items()
        Inventory().early_item()

    def menu_shop(self):
        shop = Shop()
        while True:
            shop.set_opc_menu((str(input(MENU_OPC_SHOP_INPUT))))
            if shop.get_opc_menu() == "1":
                shop.buy_items(self.get_character_selected())
            elif shop.get_opc_menu() == "2":
                shop.sell_items(self.get_character_selected())
            elif shop.get_opc_menu() == "3":
                break
            else:
                print(ERROR_IN_OPC_MENU)

    def menu_inventory(self, character_selected):
        inventory = Inventory()
        while True:
            inventory.set_opc(str(input(MENU_OPC_INVENTORY_INPUT)))
            if inventory.get_opc() == "1":
                inventory.select_item_to_hand(character_selected)
            elif inventory.get_opc() == "2":
                self.menu_shop()
            elif inventory.get_opc() == "3":
                break
            else:
                print(ERROR_IN_OPC_MENU)