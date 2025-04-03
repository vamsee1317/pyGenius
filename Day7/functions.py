# Function :
# Function is a block of code which performs a specific task, when ever it is invoked or called.
# Function is a reusable block of code.
# Function is a block of code which can be called multiple times from different parts of the program. (WORA).

# Why do we need ?

# 1. Code Reusability : write once, use multiple times.
# 2. Code Readability : easy to understand.
# 3. Code Maintainability : easy to modify.
# 4. Code Scalability : easy to extend.
# 5. Code Testability : easy to test.


# Types of functions :
# 1. User Defined functions
# 2. Built-in functions
# 3. Lambda functions 


# UserDefined functions :

# Syntax :
    # def function_name():
        #     function body
# calling a function
# function_name()

# Static Functions:

# def greet():
#     print("Hello, How are you?")

# greet()
# greet()
# greet()

# Dynamic Functions :
# Function with parameters

def greet(user):
    print(f"Hello, {user} How are you?")

greet("Vamsee")
greet("Rahul")
greet("Suresh")

# Function with return value.

def add(a, b):
    print(a + b)
    return a + b
    print(a + b)

result = add(10, 20)
print(result)

# Function with default arugments


def greet(user="Guest"):
    print(f"Hello, {user} How are you?")

greet("Vamsee")
greet()

# Function with multiple Parameters :
def greet(user, age):
    print(f"Hello, {user} How are you? You are {age} years old")
   
greet("Vamsee", 25)
greet("Rahul", 30)


# Function returning multiple values

def calculate(a, b):
    sum = a + b
    difference = a - b
    product = a * b

    return sum, difference, product

sum, diff, mul = calculate(30, 20)
print(f"Sum : {sum}, Difference : {diff}, Product : {mul}")

# Using a function inside a loop :


def isEven(num):
    return num % 2 == 0

print(isEven(10))

for num in range(1, 21):
    if isEven(num):
        print(f"{num} is even")


# BuiltIn Functions :
# 1. len() : Returns the length of a string, list, tuple, dictionary
# 2. type() : Returns the type of a variable
# 3. str() : Converts a variable to a string
# 4. int() : Converts a variable to an integer
# 5. float() : Converts a variable to a float
# 6. max() : Returns the maximum value in a list
# 7. min() : Returns the minimum value in a list
# 8. sum() : Returns the sum of all values in a list
# 9. sorted() : Returns a sorted list
# 10. reversed() : Returns a reversed list
# 11. enumerate() : Returns a list of tuples containing the index and value of each item
# 12. zip() : Returns an iterator of tuples containing the values from each list


# Lambda Functions :
# Lambda functions are small anonymous functions that can take any number of arguments, but can only take one expression.
# They are used to create small functions that can be used immediately.
# They are often used in combination with higher-order functions like map(), filter(), and reduce().

# Syntax : lambda args : expression

add = lambda a, b : a + b
print(add(10, 20))


# Redbus ticket price calculator :

def calculateTicketPrice(seats, pricePerSeat, discount=0):
    totalPrice = seats * pricePerSeat
    discountAmount = totalPrice * (discount / 100)
    finalPrice = totalPrice - discountAmount
    return finalPrice

print(calculateTicketPrice(5, 100, 10))