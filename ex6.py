# the variable is assigned the value of a string 
x = "There are %d types of people." % 10
# the variable is assigned the value of a string 
binary = "binary"
# the variable is assigned the value of a string 
do_not = "don't"
# the variable is assigned the value of a string 
y = "Those who know %s and those who %s." % (binary, do_not)

# this line proints the variable x
print(x)
# this line prints the variable y
print(y)

# this line prints a string using a format character
print("I said: %r." % x)
# this line prints a string using a format character
print("I also said: '%s'." % y)

# this variable is assigned a boolean value
hilarious = False
# this variable is assigned a string with a format character
joke_evaluation = "Isn't that joke so funny?! %r"

# this line prints a string variable
print(joke_evaluation % hilarious)

# this variable is assigned a string value
w = "This is the left side of..."
# this variable is assigned a string value
e = "a string with a right side"

# this line prints the concatenated string
print(w + e)