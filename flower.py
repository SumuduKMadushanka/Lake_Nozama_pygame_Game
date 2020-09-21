## Created by : Sumudu Madushanka
## Python version  :  Python 3.8.5

from display_functions import display_popup_messages

class Flower:
    def __init__(self, name):
        self.__name = name
        self.__cordinate = None

    def getName(self):
        return self.__name

    def setCordinate(self, cordinate):
        self.__cordinate = cordinate
    def getCordinate(self):
        return self.__cordinate

class LotusFlower(Flower):
    def __init__(self):
        super().__init__("LFL")
        self.__petals = 100

    def getPetals(self):
        return self.__petals

    def pluckPetals(self, petals):
        self.__petals -= petals

class DangerFlower(Flower):
    def __init__(self, damage):
        super().__init__("DFL")
        self.__damage = damage

    def getDamage(self):
        return self.__damage

    def attack(self, player):
        player.attacked(self.__damage)
        display_popup_messages(f"Danger Flower attacked {player.getName()}")

class KillerFlower(Flower):
    def __init__(self):
        super().__init__("KFL")

    def kill(self, player):
        player.die()

    def attack(self, player):
        self.kill(player)
        display_popup_messages(f"Killer Flower killed {player.getName()}")