# number of cars
cars = 100
# capacity of a car
space_in_a_car = 4
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# number of cars not driven as the number of cars minus the number of drivers
cars_not_driven = cars - drivers
# set the number of cars driven to the number of drivers
cars_driven = drivers
# set carpool capacity to the number of cars driven times the capcity of a car
carpool_capacity = cars_driven * space_in_a_car
# set the average number of passengers in a 
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "people today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")