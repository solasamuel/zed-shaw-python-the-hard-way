# i = 0
# numbers = []
# count = 6

# while i < count:
#     print("At the top i is %d" % i)
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)

#     print("At the bottom i is %d" % i)


# print("The numbers: ")

# for num in numbers:
#     print(num)

# def ex33(count, increase):
#     i = 0
#     numbers = []

#     while i < count:
#         print("At the top i is %d" % i)
#         numbers.append(i)

#         i = i + increase
#         print("Numbers now: ", numbers)

#         print("At the bottom i is %d" % i)


#     print("The numbers: ")

#     for num in numbers:
#         print(num)



def ex33(count, increase):
    i = 0
    numbers = []

    for i in range(0, count, increase):
        print("At the top i is %d" % i)
        numbers.append(i)

        # i = i + increase
        print("Numbers now: ", numbers)

        print("At the bottom i is %d" % i)


    print("The numbers: ")

    for num in numbers:
        print(num)

ex33(81, 9)