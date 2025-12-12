from shapes import Triangle, Circle, Rectangle
from dataInput import DataInput

#A program levezető része

class ShapesManager(Triangle, Circle, Rectangle, DataInput):
    def __init__(self):
        self.mainMenuItems = "[1] Háromszög:[2] Kör:[3] Téglalap:[4] Kilépés"
        self.areaMenuItems = "[1] Kerület:[2] Terület:[3] Mégse"
        self.mainMenuSp = self.mainMenuItems.split(":")
        self.areaMenuSp = self.areaMenuItems.split(":")

    def setMainMenuItems(self):
        for item in self.mainMenuSp:
            print(item)

    def setAreaMenuItems(self):
        for item in self.areaMenuSp:
            print(item)

    def controller(self):
        while(True):

            self.setMainMenuItems()
            choice = self.getInt("Válassz: ")
            
            match(choice):

                case 1:
                    print("Háromszög")
                    self.getTriSides()
                    self.chooseMethodTriangle()
                case 2:
                    print("Kör")
                    self.getCircRad()
                    self.chooseMethodCircle()
                case 3:
                    print("Téglalap")
                    self.getRectSides()
                    self.chooseMethodRectangle()
                case 4:
                    print("Kilépés. . .")
                    exit()
                case __:
                    print("Hibás választás. Válassz újra! (1 - 4) ")

#A program kimenete
    
print("\n--- Síkidom kerület / terület számító ---\n")
manager = ShapesManager()
manager.controller()