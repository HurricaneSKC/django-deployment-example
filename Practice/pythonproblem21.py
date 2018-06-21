# getters and setters

class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

# heigth getter
    @property
    def height(self):
        print("Get height")

        return self.__height

# height setter

    @height.setter
    def height(self, value):

        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

# width getter

    @property
    def width(self):
        print("Get height")

        return self.__width

# width setter

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")


    def getArea(self):
        return int(self.__width) * int(self.__height)

def main():
    aSquare = Square()

    height = input("Enter Height: ")
    width = input("Enter Width: ")

    aSquare.height = height
    aSquare.width = width

    print("Height: ", aSquare.height)
    print("Width: ", aSquare.width)

    print("The area is: ", aSquare.getArea())

main()

