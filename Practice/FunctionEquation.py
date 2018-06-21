# Problem 10: Create an equation solver, functions
# solve for x
# x + 4 = 9
# x will always be the first value recieved and you will only deal with addition


# Create a function that takes an input equation as a string to solve for x as above example
def string_function(equation):

# separate the function using the split operator
    x, add, num1, equals, num2 = equation.split()

# convert the string into integers
    num1 = int(num1)
    num2 = int(num2)

# solve equation
    x = num2 - num1

# return x
    return("x = {}" .format(x))

# Run function
print(string_function(input("Input function: ")))




