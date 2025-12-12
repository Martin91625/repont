import re

#Bemenet kezelő és regex

class DataInput:
    def __init__(self):
        pass

    def getString(self, text):
        inText = input(text)
        return inText

    def getInt(self, text):
        numberStr = input(text)
        while(not re.match("[0-9]+$", numberStr)):
            print("Hibás adat. Egy pozitív egész számot adjon meg! ")
            numberStr = input(text)
        number = int(numberStr)
        return number

    def getFloat(self, text):
        numberStr = input(text)
        while(not re.match("[0.-9.]+$", numberStr)):
            print("Hibás adat. Egy pozitív valós számot adjon meg! ")
            numberStr = input(text)
        number = float(numberStr)
        return number