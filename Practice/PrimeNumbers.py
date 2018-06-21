#  Create function to return a list of prime numbers
#  A prime number is a number that can only be divided by 1 and itself

# Function to find out if a number is prime taking one number a an argument
def is_prime(num):

# ignoring '1', using a 'for loop in range' we loop through each number looking for modulus 0
# as this would mean a number is divisible by more than itself and one and hence we need to return False
# otherwise we return True

    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True

# To allow the user to search for a list of prime numbers upto a certain value we...

def getPrimes(max_number):

# open a list
    list_of_primes = []

# loop through every number in the from the user number down to 1 testing if each one is prime using the
# is_prime function written above for each number determining is it is prime
    for num1 in range(2, max_number):
        if is_prime(num1):

# if it is we add (append) it to the list_of_primes
            list_of_primes.append(num1)

# finally returning the list
    return list_of_primes

# then we create a statment to run the functions for a user
max_num_to_check = int(input("search for primes upto: "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:

# finally printing each prime number below the users maximum
    print(prime)