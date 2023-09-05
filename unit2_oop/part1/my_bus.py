from p1_classes import Person


class Bus:
    passengers: list[Person]

    def __init__(self, driver: Person, seats: int, standing_room: int, stops: list[str]):
        self.driver = driver
        self.seats = seats
        self.standing_room = standing_room
        self.stops = stops
        self.passengers = []

    def get_driver(self):
        return self.driver

    def get_passengers(self):
        return self.passengers

    def get_seats(self):
        return self.seats

    def get_standing_room(self):
        return self.standing_room

    def get_stops(self):
        return self.stops

    def add_passenger(self, passenger: Person):
        self.passengers.append(passenger)

    def remove_passenger(self, passenger: Person):
        self.passengers.remove(passenger)

    def add_stop(self, stop: str):
        self.stops.append(stop)

    def remove_stop(self, stop: str):
        self.stops.remove(stop)

    def get_num_passengers(self):
        return len(self.passengers)

    def get_num_stops(self):
        return len(self.stops)

    def __str__(self):
        return f"Driver: {self.driver}\nPassengers: {self.passengers}\nSeats: {self.seats}\nStanding Room: {self.standing_room}\nStops: {self.stops}\n"

class SchoolBus(Bus):
    def __init__(self, driver: Person, seats: int, standing_room: int, stops: list[str], school: str, bus_number: int):
        super().__init__(driver, seats, standing_room, stops)
        self.school = school
        self.bus_number = bus_number

    def get_school(self):
        return self.school

    def get_bus_number(self):
        return self.bus_number

    def __str__(self):
        return f"Driver: {self.driver}\nPassengers: {self.passengers}\nSeats: {self.seats}\nStanding Room: {self.standing_room}\nStops: {self.stops}\nSchool: {self.school}\nBus Number: {self.bus_number}"