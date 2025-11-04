import re

def getString(text):
    inText=input()
    return inText
def getInteger(text):
    numberStr=input(text)
    while(not (re.match("[0-9]+$",numberStr))):
        print("Hibás adat!")
        numberStr=input(text)
    number= int(numberStr)
    return number
def getFloat(text):
    numberStr=input(text)
    while(not re.match("[0.-9.]+$",numberStr)):
        print("Hibás adat!")
        numberStr=input(text)
    number=float(numberStr)
    return number