from random import randint

class Car:
    """
    Class for Cars.

    Access modifier rationale:
    self.model is public to allow access in class Mechanic.
    self.repaired is public to allow access in class Garage.
    """

    top_speed = 260

    def __init__(self, model):
        self.model = model
        self.repaired = False

    def check_status(self):
        if self.repaired:
            print(f"The {self.model} is in good condition!")
        else:
            print(f"The {self.model} needs to be fixed!")

    def test_drive(self):
        if self.repaired:
            speed = randint(50, Car.top_speed / 2)
            print(f"Went for a test drive in the {self.model} at {speed} km/h!")
        else:
            print(f"The {self.model} needs to be fixed before a test drive!")

class Supercar(Car):
    """Cars subclass for Supercars."""

    top_speed = 340

    def test_drive(self):
        if self.repaired:
            speed = randint(100, Supercar.top_speed / 2)
            print(f"Went for a test drive in the {self.model} at {speed} km/h!")
        else:
            print(f"The {self.model} needs to be fixed before a test drive!")

    def burnout(self):
        if self.repaired:
            self.repaired = False
            print(f"Oops! Now the {self.model} needs new tires :(...")
        else:
            print(f"The {self.model} needs to be fixed first!")
