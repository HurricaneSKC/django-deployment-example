# using random module to create random number list
import random
import math

# Opening up a list
randlist = []

# running a for loop to determine how many numbers are required in the list e.g. 5
for i in range(5):

    # using random number generator to select the numbers out from 1 to 9
    i = random.randint(1, 10)

    # appending number to list
    randlist.append(i)

# printing list
print(randlist)

