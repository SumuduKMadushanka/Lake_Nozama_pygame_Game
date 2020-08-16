## Created by : Sumudu Madushanka
## Last update : 8/16/2020

from display_functions import display_special_messages

class Treasure:
    def __init__(self):
        self.__name = "TR"
        self.__cordinate = None
        self.__winner = None

    def getName(self):
        return self.__name

    def setCordinate(self, cordinate):
        self.__cordinate = cordinate
    def getCordinate(self):
        return self.__cordinate

    def takenTreasure(self, winner):
        self.__winner = winner
        self.__cordinate.removeObject()
        display_special_messages(f"{self.__winner.getName()} take the Treasure")
        display_special_messages(f"{self.__winner.getName()} Won the Game")

    def getWinner(self):
        return self.__winner