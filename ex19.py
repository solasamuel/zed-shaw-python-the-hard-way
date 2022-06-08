# # this line defines a function and its arguments
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     # this line prints out a formatted string with the first agrument variable
#     print("You have %d cheeses!" % cheese_count)
#     # this line prints out a formatted string with the second agrument variable
#     print("You have %d boxes of crackers!" % boxes_of_crackers)
#     # this line prints out a string
#     print("Man, that's enough for a party!")
#     # this line prints out another string
#     print("Get a blanket.\n")

# # this line prints out a string
# print("We can just give the function numbers directly:")
# # this line runs the function with number arguments
# cheese_and_crackers(20, 30)

# print("OR, we can use variables from out script:")
# # these two lines define variables
# amount_of_cheese = 10
# amount_of_crackers = 50

# # this line runs the function with variable arguments
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print("We can even do the math inside too:")
# # this line runs the fucntion with expressions as an argument
# cheese_and_crackers(10 + 20, 5 + 6)

# print("And we can combine the two, variables and math:")
# # this line runs the function with expressions including variables as an argument
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# similar function

def pancakes_and_sausages(number_of_pancakes, number_of_sausages):
    print("You have %d pancakes! " % number_of_pancakes)
    print("Your have %d sausages!" % number_of_sausages)
    print("It's time for breakfast.")
    print("Bon Apetit! \n")

print("By passing numbers in directly...")
pancakes_and_sausages(30, 50)

print("By passing in variables...")
amount_of_pancakes = 40
amount_of_sausages = 45
pancakes_and_sausages(amount_of_pancakes, amount_of_sausages)

print("By passing in a mix of variables and numbers...")
pancakes_and_sausages(amount_of_pancakes, 55)
pancakes_and_sausages(30, amount_of_sausages)

print("By passing in expressions...")
pancakes_and_sausages(2 * 12, 3 * 6)
pancakes_and_sausages(4 * 5, 6 + 6)
pancakes_and_sausages(4 + 5, 8 - 6)

print("By passing in expressions of variables...")
pancakes_and_sausages(2 * amount_of_pancakes, amount_of_sausages - 3)
pancakes_and_sausages(amount_of_pancakes / 10, amount_of_sausages * 2)
pancakes_and_sausages(amount_of_pancakes - 5, amount_of_sausages - 10)