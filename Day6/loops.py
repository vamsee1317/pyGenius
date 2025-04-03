# Loops :
# Loops in python allow us to execute a block of code multiple times without re-writing the code.
# There are two types of loops in python :
# 1. For loop - iterates over a sequence of list, tuple, set, string..etc
# 2. While loop - repeats as long as the condition is true
# 3. Nested loops - loop inside another loop



# Example for for loop : Display available bus routes

busRoutes = ["Hyd-Bng", "Hyd-Mum", "Hyd-Che", "Hyd-Klt"]

# print(busRoutes[0])
# print(busRoutes[1])
# print(busRoutes[2])
# print(busRoutes[3])
# print(busRoutes[4])

print("Available Routes")
for route in busRoutes:
    print(f"- {route}")


# While Loop - check seat availability:

availableSeats = 10

while availableSeats > 0:
    print(f"Booking is confirmed : Available Seats : {availableSeats}")
    if availableSeats < 5:
        print(f"Huury last {availableSeats} left")
    availableSeats -= 1

print("No seats available")


# Nested Loops :

# Showing no of seats in a bus layout

rows = 3
columns = 4


for row in range(1, rows + 1):
    for seats in range(1, columns + 1):
        print(f"Seat {seats}", end=" ")

    print()  # print() is used to print a new line

# left angle traingle
# *
# * *
# * * *
# * * * *
# * * * * *

# Right angle triangle:
#          *
#        * *
#      * * *
#    * * * *
#  * * * * *

# Break & continue :

busRoutes = ["Hyd-Bng", "Hyd-Mum", "Hyd-Che", "Hyd-Klt"]

for bus in busRoutes:
    if bus == "Hyd-Mum":
        print("Found the bus")
        break
    print("checking for bus....")
    