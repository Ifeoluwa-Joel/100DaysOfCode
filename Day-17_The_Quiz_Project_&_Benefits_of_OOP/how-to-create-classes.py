"""TUTORIAL FILE"""

class Car:
    def __init__(self, seats, color, model):
        self.seats = seats
        self.color = color
        self.model = model

    def enter_race_mode(self):
        self.seats = 2
        return self.seats

    def change_colour(self):
        new_color = input("What color do you want? ")
        self.color = new_color
        return self.color

    def change_seat_nos(self):
        new_seat_nos = int(input("How many seats does the car have? "))
        self.seats = new_seat_nos
        return self.seats


car001 = Car(9, 'Black', 'Chevy')
print(f" Seats before car entered race mode: {car001.seats}")
car001.enter_race_mode()
print(f" Seats after car entered race mode: {car001.seats}")
