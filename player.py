## Created by : Sumudu Madushanka
## Last update : 8/16/2020

from instrument import Fin, Binocular
from flower import LotusFlower
from display_functions import display_special_messages

class Player:
    __map = None

    def __init__(self, name):
        self.__name = name
        self.__health = 100
        self.__fins = [Fin("Left"), Fin("Right")]
        self.__binocular = Binocular()
        self.__cordinate = None
        self.__treasure = None
    
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def eatenFins(self):
        self.__fins = [None, None]
    def hasFins(self):
        if self.__fins[0] != None and self.__fins[1] != None:
            return True
        return False
    
    def getBinocular(self):
        return self.__binocular
    def hasBinocular(self):
        if self.__binocular != None:
            return True
        return False
    def stolenBinocular(self):
        self.__binocular = None
    
    def setCordinate(self, cordinate):
        self.__cordinate = cordinate
    def getCordinate(self):
        return self.__cordinate

    def swim(self, direction):
        current_x = self.__cordinate.getX()
        current_y = self.__cordinate.getY()

        around = {
            "up" : [current_x, current_y + 1],
            "down" : [current_x, current_y - 1],
            "left" : [current_x - 1, current_y],
            "right" : [current_x + 1, current_y]
        }

        Player.__map.getCordinate(around[direction][0], around[direction][1]).setPlayer(self)
        Player.__map.getCordinate(current_x, current_y).removePlayer()

        if self.__health < 100:
            self.searchForLotus()

    def takeTreasure(self, treasure):
        self.__treasure = treasure
        treasure.takenTreasure(self)
    def hasTreasure(self):
        if self.__treasure != None:
            return True
        return False
    def getTreasrue(self):
        return self.__treasure

    def attacked(self, damage):
        new_health = self.__health - damage
        if new_health <= 0:
            self.die()
        else:
            self.__health = new_health

    def die(self):
        self.__health = 0
        self.__cordinate.removePlayer()

    def searchForLotus(self):
        if isinstance(self.__cordinate.getObject(), LotusFlower):
            self.pluckLotusPetals(self.__cordinate.getObject())

    def pluckLotusPetals(self, lotus_flower):
        if lotus_flower.getPetals() > 0:
            petal_taken = min(100 - self.__health, lotus_flower.getPetals())
            self.__health += petal_taken
            lotus_flower.pluckPetals(petal_taken)
            display_special_messages(f"{self.getName()} pluck {petal_taken} Lotus Petals")

    def useBinocular(self):
        return self.__binocular.serchAround(Player.__map, self.__cordinate)
    
    @classmethod
    def setMap(cls, map):
        cls.__map = map

    @classmethod
    def getMap(cls):
        return cls.__map