from . import availableRoutes, updateSeats


def bookTicket(name, busNo, seats):
    buses = availableRoutes()

    if busNo not in buses:
        print("No bus avalable")
        return None
    

    if buses[busNo]["available_seats"] >= seats:
        updateSeats(busNo, seats)
        print(f"Ticket booked for {name} in bus {busNo} with {seats} seats.")
        return {
            "name" : name,
            "busNo" : busNo,
            "seats" : seats,
            "route" : buses[busNo]["route"]
        }
    else:
        print("Not enough seats available")
        return None