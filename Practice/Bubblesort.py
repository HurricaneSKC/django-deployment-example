import math
import random

# Bubble: sort random list with checking statements

# create random number list
randlist = []

for i in range(6):
    i = random.randint(1, 10)
    randlist.append(i)

print(randlist)

# set i to the 1 less the length of the list to get the max index value
i = len(randlist) - 1

# start a while loop where i is greate than 1 where i will be later decremented to start the loop again
while i > 1:
    
    # index j
    j = 0

# where j is less than i run loop until j is is incremented
    while j < i:

        # simple print statement allowing the user to see what the programme is comparing
        print("\n is {} > {}".format(randlist[j], randlist[j+1]))

        # if statement to compare the two numbers next to each other in the list
        if randlist[j] > randlist[j+1]:

            # if the index starting at j is > than the index of j+1 we need to switch the positions of the indexs
            print("Switch")

            # formula to switch the index numbers around
            temp = randlist[j]
            randlist[j] = randlist[j + 1]
            randlist[j + 1] = temp

        # handling index j is < index j+1 don't switch
        else:
            print("Don't Switch")

        # increment j so move to next number in the list
        j += 1

        # after each run through print the current list
        for k in randlist:
            print(k, end = ", ")
        print()

    print("End of round")

    # decrement i by 1 for a new round
    i -= 1

# once all conditions met print finished list
for k in randlist:
    print(k, end = ", ")
print()

