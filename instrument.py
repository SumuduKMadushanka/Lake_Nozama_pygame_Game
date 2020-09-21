## Created by : Sumudu Madushanka
## Python version  :  Python 3.8.5

from flower import LotusFlower

class Binocular:
    def serchAround(self, MAP, initial_position):
        in_x = initial_position.getX()
        in_y = initial_position.getY()
        around = {
            "up" : [in_x, in_y + 1],
            "down" : [in_x, in_y - 1],
            "left" : [in_x - 1, in_y],
            "right" : [in_x + 1, in_y]
        }
        has_lotus = {
            "up" : False,
            "down" : False,
            "left" : False,
            "right" : False
        }

        for key in around.keys():
            if MAP.hasCordinate(around[key][0], around[key][1]):
                if MAP.getCordinate(around[key][0], around[key][1]).hasObject():
                    if isinstance(MAP.getCordinate(around[key][0], around[key][1]).getObject(), LotusFlower):
                        has_lotus[key] = True
        return has_lotus

class Fin:
    def __init__(self, fin_type):
        self.__fin_type = fin_type

    def getFinType(self):
        return self.__fin_type