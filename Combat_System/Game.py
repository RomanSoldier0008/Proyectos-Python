from Character_enemy_controller import *
from random import randint
from time import sleep

damages = (0, 0, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4)


class Game:
    def __init__(self, character, enemy, turn=randint(1, 10)):
        self.character = character
        self.enemy = enemy
        self.turn = turn

    def game_start(self):
        global j
        count_turn_attack_enemy = 0
        len_enemies = len(self.enemy)
        while len(self.enemy) != 0 or self.character.vitality != 0:
            if len(self.enemy) == 0:
                print(HERO_WIN)
                break
            follow = True
            self.turn += 1
            if self.turn % 2 == 0:  # Si modulo 2 nos da 0 entonces es turno del enemigo. Sino de nuestro héroe.
                print(TURN_OF_ENEMY)
                sleep(3)
                dice_enemy = randint(0, 11)
                damage_enemy = damages[dice_enemy]
                damage_total_enemy = (self.enemy[count_turn_attack_enemy].strength // self.character.agility) \
                                     + damage_enemy
                self.character.vitality -= damage_total_enemy
                print(f"""
{ENEMY} ah realizado : {damage_total_enemy} de daño!
Dejando a {self.character.name} con vitalidad en: {self.character.vitality}
""")
                sleep(4)
                if self.character.vitality <= 0:
                    print(HERO_DEAD)
                    sleep(2)
                    break
                else:
                    print(HERO_LIVE)
                    sleep(2)
            else:
                if self.character.vitality > 0:
                    print(TURN_OF_PLAYER)
                    sleep(3)
                    while follow:
                        for j in range(len(self.enemy)):
                            print("######### ENEMIGO NÚMERO: {} #########\n{}\n######### ENEMIGO NÚMERO: {} #########\n"
                                  .format(j, self.enemy[j], j))
                            sleep(2)
                        select_enemy_to_attack = int(input(SELECT_ENEMY_TO_ATTACK_INPUT))
                        if select_enemy_to_attack < 0 or select_enemy_to_attack > (len_enemies - 1):
                            print(NO_ENEMY_SELECT_WITH_THAT_NUMBER)
                            sleep(2)
                            self.turn = 2
                            break
                        else:
                            str(input(ROLL_DICE_INPUT))
                            dice = randint(0, 11)
                            damage = damages[dice]
                            damage_total = (self.character.strength // self.enemy[select_enemy_to_attack].agility) + \
                                           damage
                            self.enemy[select_enemy_to_attack].vitality -= damage_total
                            print(f"""
Has realizado : {damage_total} de daño!
Dejando al {ENEMY} con vitalidad en: {self.enemy[select_enemy_to_attack].vitality}""")
                            sleep(4)
                            if self.enemy[select_enemy_to_attack].vitality <= 0:
                                self.enemy.pop(select_enemy_to_attack)
                                print(ENEMY_DEAD)
                                sleep(2)
                            else:
                                print(ENEMY_LIVE)
                                sleep(2)
                            follow = False
                else:
                    print(HERO_DEAD)
                    sleep(2)
                    break
