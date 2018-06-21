# ---------- PROBLEM : COMPOUNDING INTEREST ----------
# Have the user enter their investment amount and expected interest and number of years they will invest
# Each year their investment will increase by investment + investment * the interest rate

# Ask user to enter the investment amount
investment = int(input("Enter investment amount: "))

# Ask user to enter the interest rate and convert to float
interest_rate = float(input("Enter interest rate: "))

# Ask user to set the number of years they would like to invest for
years = int(input("Enter number of years: "))

# Convert interest into a percentage
interest_rate = interest_rate * 0.01

# using a for loop we cycle through 10 instances of the compounding interest formula
for i in range (years):
    investment = investment + (investment * interest_rate)

# print result to 2 decimal places
print ("{:.2f}".format(investment))


