# Conditional Statements :
# CS in python allows us to execute the block of code based on certain conditions.
# We can use if, elif, else and nested statements in python.

# These CS includes:
# 1. if statement - executes a block of code if a condition is true.
# 2. if-else statement - executes one block if True, another block if it is False
# 3. if-elif-else statement - checks multiple conditions sequentially
# 4. nested if statement - one if inside another

# Syntax as follows :

# if statement
    # if condition:
    #     # code to be executed if condition is true

# if-else statement :
    # if condition:
    #     # code to be executed if condition is true
    # else:
    #     # code to be executed if condition is false

# if-elif-else statement :
    # if condition1:
    #     # code to be executed if condition1 is true
    # elif condition2:
    #     # code to be executed if condition1 is false and condition2 is true
    # else:
    #     # code to be executed if both condition1 and condition2 are false

# Nested if statement :
# if condition1:
#     if condition2:
#         # code to be executed if both conditions are true
#     else:
#         # code to be executed if condition1 is true and condition2 is false
# else:
#     # code to be executed if condition1 is false


# if True:
#     print("Condition is true")
#     if True:
#         print("Condition inside if is true")
#     else:
#         print("Condition inside if is false")
# else:
#     print("Condition is false")

# if Statement - checking availability of seats
availableSeats = 5

if availableSeats > 0:
    print("Seats are available")


# if-else statement - payment status check

paymentStatus = "Sucess"

if paymentStatus == "Sucess":
    print("Payment is successful")
else:
    print("Payment is fialed! Try again")

# if-elif-else statement - applying discount based on user type

userType = "Premium"

if userType == "firstTimeUser":
    print("Discount is 10%")
elif userType == "Premium":
    print("Discount is 20%")
else:
    print("No discount available")

# Checking age of a person for voting based age & location:

age = 25
location = "TG"


if age >= 18 and location == "TG":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Nested if statements

busType = "AC"
seatsAvailable = 10

if busType == "AC":
    if seatsAvailable > 0:
        print("AC bus is available! proceed with your booking")
    else:
        print("AC bus is fully booked! Try another bus type")
else:
    if availableSeats > 0:
        print("Non-AC bus is available! proceed with your booking")
    else:
        print("Non-AC bus is fully booked! Try another bus type")