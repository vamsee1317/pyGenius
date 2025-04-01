# Operators :

#   - Arithmetic operators: +, -, *, /, %

# Redbus example for arithmetic operators :

ticketPrice = 1500
ticketsBooked = 2

totalAmount = ticketPrice * ticketsBooked
serviceCharges = totalAmount * 0.05
walletAmount = 200
finalAmount = (totalAmount + serviceCharges) - walletAmount  # BODMAS

print("Total amount : ", totalAmount)
print("Service charges : ", serviceCharges)
print("Final amount : ", finalAmount)


num1 = 1000
num2 = 20

# modulus vs division
print("Modulus : ", num1 % num2)
print("Division : ", num1 / num2)  # in python 3, division returns



# Comparision Operators :

#   - Equal to : ==
#   - Not equal to : !=
#   - Greater than : >
#   - Less than : <
#   - Greater than or equal to : >=
#   - Less than or equal to : <=


userAge = 65
promoCode = "BUS50"

if userAge >= 50:
    seniorCitizenDiscount = finalAmount * 0.1
    print("Senior citizen discount : ", seniorCitizenDiscount)

if promoCode == "BUS50":
    promoCodeDis = 50
    print("Promo code applied : ", promoCode)

noOfTicketsBooked = 6

if noOfTicketsBooked > 5:
    groupDicount = finalAmount * 0.25
    print("Group discount : ", groupDicount)

if ticketsBooked < 0:
    print("Invalid number of tickets booked")

# Not equals example with date

# Assignment Operators
#   - Assign : =
#   - Add and assign : +=
#   - Subtract and assign : -=
#   - Multiply and assign : *=
#   - Divide and assign : /=
#   - Modulus and assign : =%
#   - Exponent and assign : **=
#   - Floor division and assign : //=

# Initial seat availability
availableSeats = 40

# availableSeats = availableSeats - ticketsBooked
availableSeats -= ticketsBooked
print("Available seats after booking : ", availableSeats)
cancelledTickets = 1
availableSeats += cancelledTickets
finalAmount *= 0.05


# Logical Operator :
#   - and   (*)
#   - or    (+)
#   - not   (Opposite)

# Truth table for and
# input1    input2      input3   ouput
# 0         0           0        0
# 0         0           1        0
# 0         1           0        0
# 0         1           1        0
# 1         0           0        0
# 1         0           1        0
# 1         1           0        0
# 1         1           1        1

# Booking conditions using and

availableSeats = 5
userVerified = True
userAge = 18

if (availableSeats > 0 and userVerified and userAge >= 18) :
    print("Booking successful")
else :
    print("Booking failed")


# Payment Options with or
#   - Credit Card
#   - Debit Card
#   - Net Banking
#   - UPI
#   - Wallet

hasCreditCard = True
hasDebitCard = False
hasNetBanking = True
hasUPI = False
hasWallet = False

if hasCreditCard or hasDebitCard or hasNetBanking or hasUPI or hasWallet :
    print("Payment successful")
else :
    print("Payment failed")


# Not Operator :
#   - It is used to negate the boolean value

# Syntax :  not expression

userLoggedIn = False

if not userLoggedIn :
    print("User is not logged in")



x = 10
y = 20


if not (x > 20 and y < 10):
    print("Condition is not met")
else:
    print("Condition is met") 


# Indentiy Operators
#   - is
#   - is not

user1 = {"name":"rahul", "ticket":"HYD123"}
user2 = {"name":"rahul", "ticket":"HYD123"}
user3 = user1

print(user1 is user2)  # False (Different memory locations)
print(user1 is user3) # True (Same memory location)
print(user1 is not user2) # True (Different Objects)

# Membership Operators
#   - in
#   - not in

loggedInUsers = ["rahul", "ramesh", "suresh", "mahesh"]
user = "umesh"

# if user in loggedInUsers:
#     print("User is available")
# else:
#     print("User is not available")

if user not in loggedInUsers:
    print("Please signUp")
else:
    print("Welcome")


availableRoutes = ["Hyd-Bng", "Hyd-Chi", "Hyd-Mum"]

userReqRoute = "Hyd-Ker"

if userReqRoute in availableRoutes:
    print("Route is available")
else:
    print("Route is not available")





# Frequently used git commands

# git init
# git status
# git add .
# git commit -m "First commit"
# git log