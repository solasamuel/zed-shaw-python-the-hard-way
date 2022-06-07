# this line imports the module for pulling argument variable
from sys import argv

# this line uses the above line to pull the argument variables
script, filename = argv

# # the following lines print strings to to teminal
# print("We're going to erase %r." % filename)
# print("If you don't want that, hit CTRL-C (^C).")
# print("If you do want that, hit RETURN.")

# # the following line prompts the user for a response
# input("?")

# print("Opening the file...")
# # the following line open a file with the defined file name
# target = open(filename, 'w')

# print("Truncation the file. Goodbye!")
# # the following line empties the file
# target.truncate()

# print("Now I'm going to ask you for three lines.")

# # the following lines prompts the user for three lines of input
# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3: ")

# print("I'm going to write these to the file.")

# # the following lines write the above lines into the target file with a newline character after each
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# print("And finally we close it.")
# # the following line closes the file
# target.close()


# similar script to read the scriptx 
print("Opening the file...")
# the following line open a file with the defined file name
target = open(filename, 'r')

print("Here are it's contents: ")
# the following line empties the file
print(target.read())