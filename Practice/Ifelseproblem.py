# Basic problem utilising if and elif statements

# Take the users age input and determine what level of education the user should be in
age = int(input("Enter your age: "))

# Handle under 5's
if age < 5:
    print("Too young for school")

# If the age is 5 Go to Kindergarten
elif age == 5:
    print ("Go to Kindergarten")

# Ages 6 through 17 goes to grades 1 through 12
elif age >= 6 and age<= 17:
    print ("go to grade {}".format(age-5))

# If age is greater then 17 say go to college
elif age > 17:
    print ("Go to college")