# Problem : Creating an Acronym generator
# allow user to enter a string like Random Access Memory and output R.A.M.

#  Ask user to input a string to be converted into an acronym
acronym_string = input("Please enter a string: ")

# Convert string into a list
string_convert = acronym_string.split()

# Cycle through the list, get first letter of the word, capitalsing each letter
for each_word in string_convert:
    print ((each_word[0]).capitalize(), end=".")


