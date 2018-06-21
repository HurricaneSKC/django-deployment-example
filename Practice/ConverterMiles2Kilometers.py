# Converter allowing the user to input a set number of miles into kilometers
# converting miles into kilometers assuming 1 mile = 1.60934 kilometers

#Statment allowing user to input the number of miles to be converted
miles = input("Please enter number of miles to be converted to kilometers: ")

#Convert input to an float
miles = float(miles)

#Calculate miles into kilometers assuming 1 mile = 1.60934 kilometers
kilometers = miles * 1.60934

# Print statement to engage user
print ("{:.2f} miles equals {:.2f} kilometers".format(miles, kilometers))

