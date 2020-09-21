## Created by : Sumudu Madushanka
## Python version  :  Python 3.8.5

from display_functions import display_popup_messages

class Fish:
    def __init__(self, name):
        self.__name = name
        self.__cordinate = None

    def getName(self):
        return self.__name

    def setCordinate(self, cordinate):
        self.__cordinate = cordinate
    def getCordinate(self):
        return self.__cordinate

class TheifFish(Fish):
    def __init__(self):
        super().__init__("TFH")

    def stealBinocular(self, player):
        if player.hasBinocular():
            player.stolenBinocular()
            display_popup_messages(f"Theif Fish stole {player.getName()}\'s Binocular")

    def attack(self, player):
        self.stealBinocular(player)

class RubberEatingFish(Fish):
    def __init__(self):
        super().__init__("REF")

    def eatFins(self, player):
        player.eatenFins()
        display_popup_messages(f"Rubber Eating Fish ate {player.getName()}\'s Fins")

    def attack(self, player):
        self.eatFins(player)

class DangerFish(Fish):
    def __init__(self, damage):
        super().__init__("DFH")
        self.__damage = damage

    def getDamage(self):
        return self.__damage

    def attack(self, player):
        player.attacked(self.__damage)
        display_popup_messages(f"Danger Fish attacked {player.getName()}")

class KillerFish(Fish):
    def __init__(self):
        super().__init__("KFH")

    def kill(self, player):
        player.die()

    def attack(self, player):
        self.kill(player)
        display_popup_messages(f"Killer Fish killed {player.getName()}")