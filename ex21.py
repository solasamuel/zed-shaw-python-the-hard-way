def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, weight, weight, iq))


# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

# 35 + (74 - (180 * (50 / 5)))
what = add(age, subtract(height, multiply(weight, divide(iq, 5))))

print("That becomes: ", what, "Can you do it hand?")

# now for the reverse
# 5 / (50 * (180 - (74 + 35)))
what_now = divide(5, multiply(iq, subtract(weight, add(height, age))))
print("for the reverse:", what_now)