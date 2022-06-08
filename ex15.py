# This line import the feature argv used to pull argument variables
from sys import argv

# this line pulls those argument variables
script, filename = argv

# the line opens a file with the filename argument
txt = open(filename)

# # this line prints out the file name and its content
# print("Here's your file %r:" % filename)
# print(txt.read())

txt.close()

# # this line prompts the user for another filename
# print("Type the filename again:")
file_again = input("filename: ")

# these lines open the file and print it's content
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()