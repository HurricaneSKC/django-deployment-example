# ---------- PROBLEM : DRAW A PINE TREE ----------
# For this problem I want you to draw a pine tree after asking the user
# for the number of rows. Here is the sample program

'''
How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #
'''

# Ask user to determine the height of the tree
tree_height = int(input("How tall is the tree : "))

# set the number of spaces from the start of the line
spaces = tree_height - 1

# set the starting number of hashes per line
hashes = 1

# spaces for the stump
stump_spaces = tree_height - 1

# Create while loop to print correct number of spaces and hashes
while tree_height > 0:

# for loop in range of spaces to print correct number of spaces
    for i in range (spaces):
        print (" ", end="")

# for loop in range of hashes to print correct number of hashes
    for i in range (hashes):
        print ("#", end="")

# print to start new line
    print()

# reduce tree height by one
    tree_height = tree_height - 1

# increase hashes by 2 each time
    hashes = hashes + 2

# reduce spaces by 1
    spaces = spaces - 1

# print spaces for stump
for i in range (stump_spaces):
    print (" ", end="")

# print stump
print ("#")


