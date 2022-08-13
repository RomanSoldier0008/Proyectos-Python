from Character import *
from Character_hero_controller import *

global name,\
    age,\
    strength,\
    agility,\
    vitality

character_hero = 0
character_enemy = 0

execute = True
while execute:
    option = int(input(OPTIONS_INPUT))
    follow = True
    while follow:
        if option == 1:
            distributed_points = False
            select_character = str(input(CHARACTER_HERO_INPUT)).strip().lower().capitalize()
            if select_character == BREED_ELF or select_character == BREED_WIZARD or select_character == BREED_DWARF:
                breed = select_character
                if select_character == BREED_ELF:
                    print(GENERATE_HERO_ELF)
                elif select_character == BREED_WIZARD:
                    print(GENERATE_HERO_WIZARD)
                elif select_character == BREED_DWARF:
                    print(GENERATE_HERO_DWARF)
                name = str(input(NAME_HERO_INPUT)).strip().lower().capitalize()
                age = int(input(AGE_HERO_INPUT))
                distributed_points = True
                while distributed_points:
                    strength = int(input(STRENGTH_HERO_INPUT))
                    agility = int(input(AGILITY_HERO_INPUT))
                    vitality = int(input(VITALITY_HERO_INPUT))
                    if strength + agility + vitality == MAX_ATRIBUTE_HERO\
                            and strength > 0\
                            and agility > 0\
                            and vitality > 0:
                        distributed_points = False
                        if select_character == BREED_ELF:
                            character_hero = Elf(breed,
                                                 name,
                                                 age,
                                                 strength,
                                                 agility,
                                                 vitality)
                            character_hero.add_atribute_power_up()
                            Character_hero_controller(character_hero).add_hero_to()
                        elif select_character == BREED_WIZARD:
                            character_hero = Wizard(breed,
                                                    name,
                                                    age,
                                                    strength,
                                                    agility,
                                                    vitality)
                            character_hero.add_atribute_power_up()
                            Character_hero_controller(character_hero).add_hero_to()
                        elif select_character == BREED_DWARF:
                            character_hero = Dwarf(breed,
                                                   name,
                                                   age,
                                                   strength,
                                                   agility,
                                                   vitality)
                            character_hero.add_atribute_power_up()
                            Character_hero_controller(character_hero).add_hero_to()
                    else:
                        print(ERROR_IN_POINTS)
                follow = False
            else:
                print(ERROR_IN_SELECT_CHARACTER)

        elif option == 2:
            print(GENERATE_ENEMY)
            number_of_enemies = int(input(NUMBER_ENEMIES_INPUT))
            for enemy in range(0, number_of_enemies):
                random_attribute_strength = randint(MIN_RANDOM_ATTRIBUTE_ENEMY,
                                                    MAX_RANDOM_ATTRIBUTE_ENEMY)
                excess = MAX_ATTRIBUTE_ENEMY - random_attribute_strength
                random_attribute_agility = randint(MIN_RANDOM_ATTRIBUTE_ENEMY,
                                                   MAX_RANDOM_ATTRIBUTE_ENEMY)
                total_excess = excess - random_attribute_agility
                random_attribute_vitality = total_excess
                random_number = randint(1, 3)
                if random_number == 1:
                    character_enemy = Elf(BREED_ELF,
                                          NAME_ENEMY_ELF,
                                          AGE_ENEMY_ELF,
                                          random_attribute_strength,
                                          random_attribute_agility,
                                          random_attribute_vitality)
                    Character_enemy_controller(character_enemy).add_enemy()
                elif random_number == 2:
                    character_enemy = Wizard(BREED_WIZARD,
                                             NAME_ENEMY_WIZARD,
                                             AGE_ENEMY_WIZARD,
                                             random_attribute_strength,
                                             random_attribute_agility,
                                             random_attribute_vitality)
                    Character_enemy_controller(character_enemy).add_enemy()
                elif random_number == 3:

                    character_enemy = Dwarf(BREED_DWARF,
                                            NAME_ENEMY_DWARF,
                                            AGE_ENEMY_DWARF,
                                            random_attribute_strength,
                                            random_attribute_agility,
                                            random_attribute_vitality)
                    Character_enemy_controller(character_enemy).add_enemy()
            follow = False

        elif option == 3:
            Character_hero_controller(character_hero).search_hero()
            follow = False

        elif option == 4:
            Character_enemy_controller(character_enemy).search_enemy()
            follow = False

        elif option == 5:
            Character_hero_controller(character_hero).character_select()
            follow = False

        elif option == 6:
            Character_hero_controller(character_hero).start_game()
            follow = False

        elif option == 7:
            print(EXIT)
            follow = False
            execute = False
        else:
            print(ERROR_BAD_OPTION)
            follow = False