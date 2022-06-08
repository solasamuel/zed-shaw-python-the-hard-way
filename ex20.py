# This line import the feature argv used to pull argument variables
from sys import argv

# this line pulls those argument variables
script, input_file = argv

# this function prints the contents of a file
def print_all(f):
    print(f.read())

# this function resets the file reader
def rewind(f):
    f.seek(0)

# this function prints out the next line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# this line opens the input file
current_file = open(input_file)

print("First, lets print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)