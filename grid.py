## Created by : Sumudu Madushanka
## Python version  :  Python 3.8.5

class Map:
    def __init__(self, len_x, len_y):
        self.__len_x = len_x
        self.__len_y = len_y
        
        self.__cordinates = []
        for i in range(self.__len_x):
            col = []
            for j in range(self.__len_y):
                cor = Cordinate(i, j)
                col.append(cor)
            self.__cordinates.append(col)
    
    def getLenX(self):
        return self.__len_x
    def getLenY(self):
        return self.__len_y

    def getCordinate(self, x, y):
        return self.__cordinates[x][y]

    def hasCordinate(self, x, y):
        if (x >= 0 and x < self.__len_x and y >= 0 and y < self.__len_y):
            return True
        
        return False


class Cordinate:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__object = None
        self.__player = None

    def __str__(self):
        return f"x: {self.__x}, y: {self.__y}"

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    def setObject(self, map_object):
        self.__object = map_object
        self.__object.setCordinate(self)
    def removeObject(self):
        self.__object = None
    def getObject(self):
        return self.__object
    def hasObject(self):
        if self.__object != None:
            return True
        return False

    def setPlayer(self, player):
        self.__player = player
        self.__player.setCordinate(self)
    def removePlayer(self):
        self.__player = None
    def getPlayer(self):
        return self.__player
    def hasPlayer(self):
        if self.__player != None:
            return True
        return False
