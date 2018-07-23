# sets a number of people types
types_of_people = 10
# sets a string with format
x = f"There are {types_of_people} types of people."

# sets a string
binary = "binary"
# also sets a string
do_not = "don't"
# sets a string with more complex format
y = f"Those who know {binary} and those who {do_not}."

# prints the result
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# sets a boolean variable
hilarious = False
# sets a text with a placeholder
joke_evaluation = "Isn't that joke so funny?! {}"
# prints a text filling the placeholder with the variable
print(joke_evaluation.format(hilarious))

# creates two string variables
w = "This is the left side of..."
e = "a string with a right side."

# prints out two string variables concatenated
print(w + e)
