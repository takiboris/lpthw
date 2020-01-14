# defines variable "cars" and sets it to 100
cars = 100
# defines "space_in_a_car" and sets it equal to 4.0
space_in_a_car = 4.0
# defines "drivers" and sets it to 30
drivers = 30
# defines the amount of "passengers"
passengers = 90
# defines "cars_not_driven" and makes it equal to cars - drivers
cars_not_driven = cars - drivers
# "cars_driven" is also equal to "cars"
cars_driven = drivers
# "carpool_capacity" is equal to the number of cars driven times the space in one
carpool_capacity = cars_driven * space_in_a_car
# defines the average passengers by dividing passengers by cars driven
average_passengers_per_car = passengers / cars_driven

# prints statements about each variable
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")