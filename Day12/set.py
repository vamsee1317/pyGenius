
# Set :
# A set is a collection of :
# - unique elements
# - unordered
# - no duplicate values
# - mutable
# - no indexing


# Creating a Set :

busStops = {"Madhapur", "Kukatpally", "Miyapur", "Madhapur", "Miyapur"}
print(busStops)

# Why sets :
# Removes duplicate values automatically
# Fast lookups
# Fast insertions and deletions


# Iterating a Set :
for stop in busStops:
    print(stop)


# Insertion :
busStops.add("JNTU")
print(busStops)

# Deletion :
busStops.remove("Miyapur")
print(f"After removing{busStops}")


# Set Operations :
# Union :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)

# intersection :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.intersection(set2)
print(set3)

# difference :
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.symmetric_difference(set2)  # 1 2 3
set4 = set2.difference(set1) # 8 6 7
print(set3)
print(set4)


# compares routes between two buses
bus1 = {"Madhapur", "Kukatpally", "Miyapur"}
bus2 = {"Madhapur", "Kukatpally", "Miyapur","JNTU", "Gachibowli", "Koti"}


commonStops = bus1 & bus2
print(f"Common stops between bus1 and bus2 are {commonStops}")


# Left over methods:
# discard() : removes an element from the set if it is a member
# pop() : removes and returns an arbitrary set element
# clear() : removes all elements from the set


