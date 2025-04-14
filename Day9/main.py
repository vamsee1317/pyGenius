# Module :
# A module is a python file(.py) contains functions, variables or classes.

# Package :
# A package is a folder that contains multiple modules and has one init.py file






# Importing packages & modules:

from bus_reservations import booking
# from bus_reservations.cancellation import cancelTicket
# from bus_reservations.payment import processPayment
# from bus_reservations.bus_info import availableRoutes, updateSeats
# from . import availableRoutes, updateSeats



from user_services.auth import registerUser, loginUser
from user_services.history import add_history, view_history

# Step 1 : register a new users:

print("Registering user....")
registerUser("vamsee", "vamse@123", "vamsee@123")


# Book a ticket
print("Booking ticket....")
booking.bookTicket("vamsee", "123", 2)
