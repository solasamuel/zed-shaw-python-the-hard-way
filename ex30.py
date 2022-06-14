# these lines assign values to the following variables
people = 60
cars = 40
buses = 70

# this line runs the adjacent code block if the stated condition is met
if cars > people:
    print("We should take the cars.")
# this line runs the adjacent code block only if the stated condition is met and the above condition is not
elif cars < people:
    print("We should not take the car.")
# this line runs the adjacent code block only if the above conditions are not met
else:
    print("We can't decide.")

# this line runs the adjacent code block if the stated condition is met
if buses > cars:
    print("That's too many buses.")
# this line runs the adjacent code block only if the stated condition is met and the above condition is not
elif buses < cars:
    print("Maybe we could take the buses.")
else:
# this line runs the adjacent code block only if the above conditions are not met
    print("We still can't decide")

# this line runs the adjacent code block if the stated condition is met
if people > buses:
    print("Alright, let's just take the buses.")
# this line runs the adjacent code block only if the above conditions are not met
else:
    print("Fine. let's just stay at home then")