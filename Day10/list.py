# List :
# List in python is used to store the collection of items into one single variable.
# List is denoted by square brackets [] and items are separated by comma(,).
# List is ordered collection of items which means item in list has index number.
# List is mutable which means list can be modified after it is created.
# List allows Duplicate values.

# It can store :
    # Numbers : [20, 30, 20]
    # Strings : ['apple', 'banana', 'cherry']
    # Boolean : [True, False]
    # NestedList : [[1, 2, 3], [4, 5,]]
    # Mixed : [1, 'apple', 3.5, True]



# Tuple :
# Tuple in python is used to store the collection of items into one single variable.
# Tuple is denoted by round brackets () and items are separated by comma(,).
# Tuple is ordered collection of items which means item in tuple has index number.
# Tuple is immutable which means tuple can not be modified after it is created.
# Tuple allows Duplicate values.



# Code related Examples :

numList = [10, 20, 30, 40, 50]
print(numList)

# Accessing list Items :

print(numList[0])  # Output : 10
print(numList[1])  # Output : 20
print(numList[2])  # Output : 30
print(numList[3])  # Output : 40
print(numList[4])  # Output : 50
print(numList[-1])  # Output : 50
print(numList[-2])  # Output : 40
print(numList[-3])  # Output : 30
print(numList[-4])  # Output : 20
print(numList[-5])  # Output : 10
print(numList[0:2])  # Output : [10, 20, 30]
print(numList[0:5])  # Output : [10, 20, 30, 40, 50]
print(numList[0:5:2]) # Output : [10, 30, 50]


# Real Time examples: 

availableRoutes = ["Hyderabad", "Bangalore", "Chennai", "Pune"]
print(availableRoutes[0])  # Output : Hyderabad"
print(availableRoutes[1])  # Output : Bangalore"
print(availableRoutes[2])  # Output : Chennai"

# Iterating a list :

for route in availableRoutes:
    print(f"Routes : {route}")

# List Methods :

# append(item) : adds an item at last position of List
availableRoutes.append("Mumbai")

# insert(index, item) : adds an item at specific position
availableRoutes.insert(2, "Kolkata")
# availableRoutes.append("Kolkata")

# remove(item) : removes the first occurrence of item
availableRoutes.remove("Kolkata")

# pop() / pop(index) : removes and returns last or specified index values
poppedItem = availableRoutes.pop()  # Output : Pune
print(poppedItem)
print(availableRoutes.pop(0))  # Output : Hyderabad

# clear() - removes all the items
availableRoutes.clear()
print(availableRoutes)# Output : []

# count(item) - returns the number of occurrences of item
availableRoutes = ["Hyderabad", "Bangalore", "Chennai", "Pune", "Bangalore", "Chennai"]
print(availableRoutes.count("Bangalore"))  # Output : 2

# index(item) : returns the first index of an item
print(availableRoutes.index("Chennai"))  # Output : 2

# sort() - sorts a list in ascending order
availableRoutes = ["Hyderabad", "Bengaluru", "Bangalore", "Chennai", "Pune"]
availableRoutes.sort()
print(availableRoutes)

fares = [999, 1399, 499, 199, 399]
fares.sort()
# sort() function sorts in ascending order by default
# reverse=True for descending order
fares.sort(reverse=True)
print(fares)

# reverse() : reverses the list
availableRoutes = ["Hyderabad", "Bengaluru", "Bangalore", "Chennai"]
availableRoutes.reverse()
print(availableRoutes)

# copy() : clones the list

backUpRoutes = availableRoutes.copy()
print(backUpRoutes)


# Usage of these methods :

booked_users = []

def book_ticket(name):
    booked_users.append(name)
    print(f"Ticket booked for {name}")


book_ticket("Vamsee")
book_ticket("Rahul")
book_ticket("Sagar")

print(booked_users)

# cancel ticket
def cancel_ticket(name):
    if name in booked_users:
        booked_users.remove(name)
        print(f"Ticket cancelled for {name}")
    else:
        print(f"No ticket booked for {name}")