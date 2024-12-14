flights = [{'flight_no': 'AI202', 'destination': 'New York'}, {'flight_no': 'AI203', 'destination': 'London'}]
reservations = []
def flight_reservation():
    print("Available flights:")
    for flight in flights:
        print(f"{flight['flight_no']} to {flight['destination']}")
    flight_no = input("Enter flight number to book: ")
    name = input("Enter your name: ")
    for flight in flights:
        if flight['flight_no'] == flight_no:
            reservations.append({'name': name, 'flight_no': flight_no})
            print(f"Reservation successful for {name} on flight {flight_no}")
            return
    print("Invalid flight number")
flight_reservation()
