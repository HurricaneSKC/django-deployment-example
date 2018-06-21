# Recursive function

# Factorial
# open up function taking in arguement num
def factorial(num):

    # factorial 1 is 1 so we use this as the first value / last value
    if num <= 1:
        return 1

    # otherwise the function works as follows
    # eg. factorial is 3
    # result = 3 * factorial(3-1 = 2)
    # so we need factorial(2) ... result = 2 * factorial(2-1 = 1)
    # we know factorial 1 = 1 so factorial(2) = 2 * 1 = 2
    # so factorial(2) = 2 so 3 * 2 = 6
    # so factorial(3) = 6

    else:

        result = num * factorial(num - 1)
        return result

print(factorial(3))

# Fibonacci numbers
# 1, 1, 2, 3, 5, 8, 13
# using a recursive function
# calc
# create function

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:

        result = fib(num - 1) + fib(num - 2)
        return result

print(fib(7))


# get fibonnaci list
def get_fiblist(num):

    num = num - 1
    x = 0
    fiblist = [0, 1]

    for i in range(num):
        y = fiblist[x] + fiblist[x+1]
        fiblist.append(y)
        x = x + 1

    return fiblist

print(get_fiblist(2))