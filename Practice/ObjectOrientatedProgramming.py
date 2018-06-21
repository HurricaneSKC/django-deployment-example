# OOP - object orientated programming

# create a class
class Dog:

    # using the __init__ (initialise function) we assign various fields
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight  = weight

    # then we define various functions
    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def barks(self):
        print("{} the dog barks".format(self.height))

# using main() to run the functions as required 
def main():
    spot = Dog("Spot")

    spot.barks()

    bowser = Dog()

    bowser.barks()




main()



