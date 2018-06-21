import math
import random

# creation of a quick list using index multiplication and a for loop
listTable = [[0] * 10 for i in range(10)]
print(listTable)

# using 2 loops within each other to change the index
for i in range(10):
    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

# using 2 loops to print and reformat
for i in range(10):
    for j in range(10):
        print(listTable[i][j], end = " || ")
    # print statement to push new line each loop
    print()

# Further table / matricies examples
# create multiples table from 1 to 10

# table creation for 10x10 table
multiple_table = [[0] * 11 for i in range(11)]

# 2 loops to replace index values with multiplication values, set the format
for i in range(1,11):
    for j in range(1,11):
        multiple_table[i][j] = "{}".format(i*j)

# 2 loops to print and format
for i in range(1,11):
    for j in range(1,11):
        print(multiple_table[i][j], end=" | ")
    print()

