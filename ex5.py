name = 'Sola O. Samuel'
age = 20 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("Which is %f centimeters." % (height * 2.54))
print("He's %d pounds heavy." % weight)
print("Which is %f kilos." % (weight * 0.4535924))
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %r %r, and %r I get %r." % (
    age, height, weight, age + height + weight))