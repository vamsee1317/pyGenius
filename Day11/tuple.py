# Tuple :
# A tuple is collection which is:
# 1. Ordered
# 2. Immutable
# 3. Indexed
# 4. Allow duplicate values
# 5. Allow heterogeneous values
# 6. Allow null values
# 7. Allow empty values


users = ("vamsee", "hari", "aagnesh")

userInfo = ("krishna", 25, "Hyd", "TG")


# Why Tuples :
# 1. Tuples are faster than lists
# 2. Tuples are more memory efficient than lists
# 3. Tuples use less memory than lists
# 4. Tuples are immutable, so they can't be changed
# 5. Tuples are used for fixed data like days, months..etc


# Accesssing Tuple Elements :

users = ("vamsee", "hari", "aagnesh")

print(users)   # Prints entire tuple
print(users[0])  # Prints first element of tuple
print(users[-1])  # Prints last element of tuple
print(users[1:3])  # Prints elements from index 1 to 3


# Immutable :
# users[0] = "VamseeKrishna"


# Looping through Tuples:

for user in users:
    print(user)


# Tuple Packing & unpacking

# Tuple Packing :
# We can pack multiple values into a tuple using the following syntax:
# tuple = (value1, value2, value3)
# Tuple Unpacking :
# We can unpack a tuple into multiple variables using the following syntax:
# (variable1, variable2, variable3) = tuple


# Packing example :

route = ("Hyderabad", "Chennai", 999)
print(route)
print(route[0])
print(route[1])
print(route[2])

# Unpacking :
fromCity, toCity, fare = route

print(fromCity)
print(toCity)
print(fare)


# Methods :
# 1. count() : Returns the number of occurrences of the specified value.
# 2. index() : Returns the index of the first occurrence of the specified value.
# 3. len() : Returns the number of items in the tuple.
# 4. max() : Returns the largest item in the tuple.
# 5. min() : Returns the smallest item in the tuple.
# 6. sorted() : Returns a new sorted list from the elements of the tuple.
# 7. tuple() : Returns a tuple created from the specified iterable or object.
# 8. reversed() : Returns a reverse iterator, yielding elements in the reverse order.


nums = (10, 20, 30, 40, 50, 60, 20)
print(nums.count(20))
print(nums.index(20))
print(len(nums))
print(max(nums))
print(min(nums))
print(sorted(nums))
print(tuple(nums))


# Real time usecase:

busTypes = ("Sleeper", "Semi-Sleeper", "AC", "Non-AC")


def showBusType():
    for index, busType in enumerate(busTypes, start=1):
        print(f"{index}. {busType}")


showBusType()