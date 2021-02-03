import random

class State():

    def __init__(self):

        self.dictionary = {(0,0): 1}

    def setCell(self, cellSelected):
        step = 0.3
        if cellSelected in self.dictionary.keys():
            value = self.dictionary.get(cellSelected)
            value -= step
            if value <= -1: 
                value = 0
            self.dictionary[cellSelected] = round(value, 1)
        else: 
            self.dictionary[cellSelected] = round(-step,1)

    def getCellValue(self, cellSelected):
        if not cellSelected in self.dictionary.keys():
            return 0
        return self.dictionary.get(cellSelected)
