import dataInput
import checker
import triangle
import rectangle
import circle

mainMenuItems="[1] Háromszög:[2] Kör:[3] Téglalap:[4] Kilépés"

def setMenuItems():
    menuSp=mainMenuItems.split(":")
    for item in menuSp:
        print(item)

def getTriSides():
    number01=dataInput.getFloat("\"A\" oldal: ")
    number02=dataInput.getFloat("\"B\" oldal: ")
    number03=dataInput.getFloat("\"C\" oldal: ")
    success=checker.checkTriangle(number01,number02,number03)
    while(not success):
        print("Hibás adat!")
        number01=dataInput.getFloat("\"A\" oldal: ")
        number02=dataInput.getFloat("\"B\" oldal: ")
        number03=dataInput.getFloat("\"C\" oldal: ")
        success=checker.checkTriangle(number01,number02,number03)
    return number01,number02,number03

def getCircRad():
    number01=dataInput.getFloat("A kör sugara: ")
    success=checker.checkCircle(number01)
    while(not success):
        print("Hibás adat!")
        number01=dataInput.getFloat("A kör sugara: ")
        success=checker.checkCircle(number01)
    return number01

def getRectSides():
    number01=dataInput.getFloat("\"A\" oldal: ")
    number02=dataInput.getFloat("\"B\" oldal: ")
    success=checker.checkRect(number01,number02)
    while(not success):
        print("Hibás adat!")
        number01=dataInput.getFloat("\"A\" oldal: ")
        number02=dataInput.getFloat("\"B\" oldal: ")
        success=checker.checkRect(number01,number02)
    return number01, number02

def main():
    while(True):
        setMenuItems()
        choose=dataInput.getInteger("Válassz: ")
        match(choose):
            case 1: 
                print("Háromszög")
                number01,number02,number03=getTriSides()
                triangle.choose(number01,number02,number03)
            case 2: 
                print("Kör")
                number01=getCircRad()
                circle.choose(number01)
            case 3:
                print("Tégla")
                number01,number02=getRectSides()
                rectangle.choose(number01,number02)
            case 4:
                print("Kilépés...")
                exit()
            case __:
                print("Hibás választás! ")
main()