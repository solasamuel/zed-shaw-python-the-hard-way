tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* %s
\t* %s
\t* %s\n\t* %s
"""

item1 = "Cat food"
item2 = "Fishies"
item3 = "Catnip"
item4 = "Grass"

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat % (item1, item2, item3, item4))