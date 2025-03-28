# Data Types :

# Examples are based on Ecommerce system

# int -> whole numbers 

mobileNumber = 8123456789
productId = 12345
orderId = 4322
quantity = 2

# Float :

price = 99.99
# print(len(price))
discount = 10.5
rating = 4.7

# String : 

customerName = "John Doe"
# print(len(customerName))
productName = "Apple iPhone 13"
orderStatus = "Shipped"
productDescription = "Best smartphone in the market"
productCategory = "Electronics"
productBrand = "Apple"
productModel = "iPhone 13"
address = "123 french colony QA"

# Boolean (True / False)

isProductAvailable = True
isOrderPlaced = False
isCustomerVerified = True
isProductInStock = False
isDiscountApplied = False
isLoggedIn = False



# list :
# list is a collection of items which can be of any data type
# list is ordered and changeable

cartItems = ["Laptop", "Mouse", "Keyboard", "Laptop"]

cartItems[1] = "JoyStick"
print(cartItems[0])
print(cartItems[1])
print(cartItems[2])
print(cartItems[3])
print(len(cartItems))

# Tuple :
# tuple is a collection of items which can be of any data type
# tuple is ordered and unchangeable
# tuple is faster than list

productCategories = ("Electronics", "Clothing", "Groceries", "Mobiles")
print(productCategories)

deliverySlots = ("Morning", "Afternoon", "Evening")
print(deliverySlots[0])

# Set :
# set is a collection of items which can be of any data type
# set is unordered and unindexed
# set is mutable
# set is used to store unique values

categories = {"Electronics", "Mobiles", "Groceries", "Mobiles"}
print(categories)

# dict 
# dict is a collection of key-value pairs

customerProfile = {
    "name" : "Jane Smith",
    "email" : "abc@gmail.com",
    "phone" : "1234567890",
    "address" : "123 french colony QA"
}
print(customerProfile["name"])


orderDetails = {
    "orderId" : "ama1234ed",
    "orderDate" : "2022-02-02",
    "orderStatus" : "placed"
}

paymentInfo = {
    "method" : "CreditCard",
    "amount" : 100.00,
    "currency" : "USD",
    "status" : ["success", "failure", "pending"],
    "method" : "DebitCard"
}

print(paymentInfo)



