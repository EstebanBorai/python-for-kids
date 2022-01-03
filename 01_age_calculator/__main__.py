# Asks user for it's name and stores it into the `name` variable
name = input('Enter your name: ')
# Asks user for it's age, then parses text into a number and
# finally stores into the `age` variable
age = int(input('Enter your age: '))
# Stores the current year into `current_year` variable.
# Note: This is HARDCODED if year changes this won't be updated
current_year = 2022

# Prints the sentence to the output
print(name + ' born on ' + str(current_year - age))
