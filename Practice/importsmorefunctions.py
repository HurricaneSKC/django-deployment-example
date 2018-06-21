# further use of functions using the math import module
import math


def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

def rectangle_area():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width

    print("area of the rectangle is: ", area)

def circle_area():
    radius = float(input("what is the radius: "))
    area = math.pi * (math.pow(radius, 2))

    print("area of the circle is {:.2f} ".format(area))


def main():
    shape_type = input("What shape would you like the areas for: ")

    get_area(shape_type)


main()