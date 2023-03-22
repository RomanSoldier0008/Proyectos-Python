from constant import RETURN_ENEMIES_FORMAT, ENEMY
class Enemies:
    def __init__(self, breed, strength, agility, vitality):
        self.__breed = breed
        self.__strength = strength
        self.__agility = agility
        self.__vitality = vitality

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

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

    def __str__(self):
        return RETURN_ENEMIES_FORMAT.format(ENEMY,
                                            self.get_breed(),
                                            self.get_strength(),
                                            self.get_agility(),
                                            self.get_vitality())

class Orc(Enemies):
    def __init__(self, breed, strength, agility, vitality):
        super().__init__(breed, strength, agility, vitality)

class Troll(Enemies):
    def __init__(self, breed, strength, agility, vitality):
        super().__init__(breed, strength, agility, vitality)

class Monster(Enemies):
    def __init__(self, breed, strength, agility, vitality):
        super().__init__(breed, strength, agility, vitality)