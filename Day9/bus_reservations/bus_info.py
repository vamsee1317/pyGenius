buses = {
    "AP39AH1234" : {
        "route" : "Hyd - Viz",
        "capacity" : 50,
        "available_seats" : 50
    },
    "TN98AH5678" : {
        "route" : "Chennai - Viz",
        "capacity" : 50,
        "available_seats" : 30
    },
    "KA25AH9012" : {
        "route" : "Bengaluru - Viz",
        "capacity" : 50,
        "available_seats" : 20
    },
    "KA25AH9013" : {
        "route" : "Bengaluru - Viz",
        "capacity" : 50,
        "available_seats" : 40
    }
}


def availableRoutes():
    return buses


def updateSeats(busNo, seatsBooked):
    if busNo in buses:
        buses[busNo]["available_seats"] -= seatsBooked
        # buses[busNo]["available_seats"] -= seatsBooked