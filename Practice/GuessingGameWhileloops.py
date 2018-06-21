# Basic guessing game
# Utilising while loops
# Guessing game between 1 and 10:

# Set variable number to be guessed

Number = 7

# As we do not know when the loop will end we need to use a while loop and set conditions for when
# the conditions are met

while True:

# Ask user to input a number to be guessed
    Guess_num = int(input("Guess a number between 1 and 10: "))

# Set condition for user guessing correctly, breaking the loop
    if Guess_num == Number:
        print("You guessed correct")
        break

# set condition if the user does not guess correct
    if Guess_num != Number:
        continue

