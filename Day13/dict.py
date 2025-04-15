
# Dictionary : 
# A dictionary is a collection of :
# Key : Value pairs
# Key is unique and immutable
# Value can be any data type
# Dictionaries are mutable
# Dictionaries are Unordered

# Syntax : 
# dict = {'key1' : 'value1', 'key2' : 'value2'}

bus_details = {
    "bus_number" : "HYD123",
    "bus_name" : "Vijay Travels",
    "bus_type" : "Sleeper",
    "bus_seats" : 50,
    "bus_route" : "Hyderabad to Bangalore",
    "bus_fare" : 1500
}

# Why Dictionaries :
# Dictionaries are used to store data in a structured way
# Dictionaries are used to store data in a key-value pair format
# Dictionaries are used to store data in a mutable way
# Dictionaries are used to store data in an unordered way
# Real world data is best represented in key-value pair


# List vs Dictionary
# List :
# List is a collection of items
# List is ordered
# List is mutable
# List is indexed
# List is a sequence of items

# Dictionary
# Dictionary is a collection of key-value pairs
# Dictionary is unordered
# Dictionary is mutable
# Dictionary is not a sequence of items

# bus_info = ["HYD123", "VijayTravels", "Sleeper"]
# print(bus_info[0])  # HYD123
# print(bus_info[1])  # VijayTravels
# print(bus_info[2])  # Sleeper

# busDetails = {
#     "bus_number" : "HYD123",
#     "bus_name" : "Vijay Travels",
#     "bus_type" : "Sleeper"
# }

# bus_details["bus_number"]



bus_details = {
    "bus_number" : "HYD123",
    "bus_name" : "Vijay Travels",
    "bus_type" : "Sleeper",
    "bus_seats" : 50,
    "bus_route" : "Hyderabad to Bangalore",
    "bus_fare" : 1500
}


# Accessing Values from Dictionary

print(bus_details["bus_name"])
print(bus_details.get("bustype"))

# .get() is safer - even if the key is not available it throws None.


# Modify the value :
bus_details["bus_fare"] = 2000
bus_details["bus_category"] = "AC"


# Remove elements

bus_details.pop("bus_category")
# del bus_details["bus_seats"]

print(bus_details)



# Looping through dictionary

for a in bus_details:
    print(f"{a} -> {bus_details[a]}")


# Nested Dictionaries :

bus_data = {
    "Hyd123" : {
        "bus_name" : "Vijay Travels",
        "bus_type" : "Sleeper",
        "bus_seats" : 50,
        "bus_route" : "Hyderabad to Bangalore",
        "bus_fare" : 1500
    },
    "Hyd456" : {
        "bus_name" : "Kaveri Travels",
        "bus_type" : "Semi-Sleeper",
        "bus_seats" : 40,
        "bus_route" : "Hyderabad to Chennai",
        "bus_fare" : 1200
    }
}


print(bus_data["Hyd456"]["bus_name"])



# methods : 

print(bus_details.keys())
print(bus_details.values())
print(bus_details.items())
print(bus_details.get("bus_fare"))
print(bus_details.pop("bus_fare"))
print(bus_details.popitem())
