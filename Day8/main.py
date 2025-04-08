# import busOperations

# busOperations.bookTickets("Vamsee", "Bangalore")
# busOperations.cancelTicket("Vamsee")

# routes = busOperations.availableRoutes()
# print(f"Available Routes : {routes}")

# from busOperations import bookTickets, cancelTicket
from busOperations import routes as routePaths
# from busOperations import cancelTicket

from busOperations import *


bookTickets("Vamsee", "Bangalore")
cancelTicket("Vamsee")
print(f"Available Routes : {routePaths}")  # Accessing the routes function from the busOperations


# Builtin Modules :
# 1. math
# 2. random
# 3. time
# 4. datetime


import math
import random
import time
import datetime

# math methods

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.ceil(3.7))
print(math.floor(3.7))
print(math.factorial(5))

# random Method
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5, 6]))
randomNumber = random.random() * 1000000
print(randomNumber)
print(math.ceil(randomNumber))

# datetime
print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y/%m %H:%M:%S"))
