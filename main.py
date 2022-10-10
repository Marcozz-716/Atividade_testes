class Coordinate:
    def __init__(self, coordinateX, coordinateY):
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY


class Quadrant:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_quadrant_coordinate(self):

        coordinateX = self.coordinates.coordinateX
        coordinateY = self.coordinates.coordinateY

        if (coordinateX > 0 and coordinateY > 0):
            return "First"
        elif (coordinateX < 0 and coordinateY > 0):
            return "Second"
        elif (coordinateX < 0 and coordinateY < 0):
            return "Third"
        elif (coordinateX > 0 and coordinateY < 0):
            return "Fourth"
        else:
            return ""



class Menu:
    def __init__(self):
        pass

    def get_user_coordinate(self):
        coordinateX = int(input("Inform the coordinate X: "))
        coordinateY = int(input("Inform the coordinate Y: "))
        self.coordinates = Coordinate(coordinateX, coordinateY)
        return self.coordinates

    def cordinate_is_valid(self, coordinates):
        if (coordinates.coordinateX == 0 or coordinates.coordinateY == 0):
            return False
        else:
            return True

    def show_menu(self):
        self.get_user_coordinate()
        return not self.cordinate_is_valid(self.coordinates)

menu = Menu()

while True:
    if (menu.show_menu() == True):
        break

    coordinates = menu.coordinates

    my_quadrant = Quadrant(coordinates)
    print(f"{my_quadrant.get_quadrant_coordinate()} quadrant.")

