import random
import math


# Create warrior class with initialise method
class Warrior:

# define attribues - name, health, maximum attack, maximum block
    def __init__(self, fname="Warrior", health="0", maxattack="0", maxblock="0" ):
        self.fname = fname
        self.health = health
        self.maxattack = maxattack
        self.maxblock = maxblock

# method to print player starting stats
#    def printplayer(self):
#       return "Name: {} Health: {} Max Attack: {}  Max Block {}".format(self.fname, self.health, self.max_attack, self.max_block)

# create attack method variable - by taking the maximum attack eg. 20 and multiply by random field (0.0 to 1.0) to create attack value

    def attack(self):

        attackval = self.maxattack * (random.random() + .5)

        return attackval

# create attack method variable - by taking the max block eg. 20 and multiply by random field (0.0 to 1.0) to create block value

    def block(self):

        blockval = self.maxblock * (random.random() + .5)

        return blockval

# create a battle class
class Battle:

# start the battle method creating a loop to know when the game has ended -  we will use this to create the Battle() object
    def thebattle(self, warrior1, warrior2):

# while loop used as an unknown number of turns will determine the winner
        while True:

# cycle between each warrior to see if the condition meet the end of the game, ending the game
            if self.attackresult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.attackresult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

# static method required as we wish to use the code to be used by both warriors to get the result of one attack verus
            # one block decrementing each warriors health as we go
    @staticmethod
    def attackresult(warriorA, warriorB):

        warriorAattackval = warriorA.attack()

        warriorBblockval = warriorB.block()

        damageWarriorB = math.ceil(warriorAattackval - warriorBblockval)

        warriorB.health = warriorB.health - damageWarriorB

# print the result of the attacks
        print("{} attacks {} and deals {} damage".format(warriorA.fname, warriorB.fname, damageWarriorB))

# print the players health after the attack
        print(" {} is down to {} health".format(warriorB.fname, warriorB.health))

# state the warriors condition following the attack
        if warriorB.health <= 0:
            print("{} has died and {} is the winner".format(warriorB.fname, warriorA.fname))

            return "Game Over"

        else:
            return "Fight Again"


def main():

    # Create 2 warriors
    player_1 = Warrior("Paul", 50, 20, 10)
    player_2 = Warrior("Steve", 50, 20, 10)

    # Create Battle object
    battle = Battle()

    # Initiate battle
    battle.thebattle(player_1, player_2)

main()

