#
# Find the multiples of 9 from a random 100 value list with
# value between 1 and 1000

import random

aList = []

for i in range(100):
    i = random.randint(1,1000)
    if i % 9 == 0:
        aList.append(i)

print(aList)

# ---------- PROBLEM ----------
# Find the multiples of 9 from a random 100 value list with
# values between 1 and 1000

# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values
randList = list(random.randint(1, 1001) for i in range(100))

# Use modulus to find multiples of 9 by passing the random
# list to filter
print(list(filter((lambda x: x % 9 == 0), randList)))

from functools import reduce

print(reduce(lambda x, y: x + y))