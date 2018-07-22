# define how many cars are available
cars = 100
# define how many seats there are in an average car
space_in_a_car = 4.0
# define how many drivers are there
drivers = 30
# define quantity of passengers
passengers = 90
# calculate how many cars will be unused
cars_not_driven = cars - drivers
# calculate how many cars will be driven
cars_driven = drivers
# calculate how many passengers can be picked up by driven cars
carpool_capacity = cars_driven * space_in_a_car
# calculate the average of passengers for a car
average_passengers_per_car = passengers / cars_driven

# print out all results
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
