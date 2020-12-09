# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Dec. 05, 2020

"""CS1.1 Assignment 3: OOP Design Challenge."""

from random import choice, randint, uniform

class Car:
    top_speed = 260

    def __init__(self, model):
        self.model = model
        self.repaired = False

    def check_status(self):
        if self.repaired:
            print(f"The {self.model} is in good condition!")
        else:
            print(f"The {self.model} needs to be reparied!")

    def test_drive(self):
        if self.repaired:
            speed = randint(50, Car.top_speed / 2)
            print(f"Went for a test drive at {speed} km/h!")
        else:
            print(f"The {self.model} needs to be fixed first!")

class Supercar(Car):
    top_speed = 340

    def test_drive(self):
        if self.repaired:
            speed = randint(100, Supercar.top_speed / 2)
            print(f"Went for a test drive at {speed} km/h!")
        else:
            print(f"The {self.model} needs to be fixed first!")

    def burnout(self):
        if self.repaired:
            self.repaired = False
            print(f"Oops :(! Now the {self.model} needs new tires...")
        else:
            print(f"The {self.model} needs to be fixed first!")

class Mechanic:
    uniform_colour = "blue"

    def __init__(self, name):
        self.name = name
        self.cars_fixed = 0

    def greet(self):
        print(f"I'm {self.name}! I wear a {Mechanic.uniform_colour} uniform and I've fixed {self.cars_fixed} cars.")

    def fix_car(self, car):
        car.repaired = True
        self.cars_fixed += 1
        print(f"{self.name} fixed the {car.model}! :)")

    @classmethod
    def change_uniform(cls, colour):
        cls.uniform_colour = colour

class Garage:
    def __init__(self):
        self.cars = []
        self.mechanics = []

    def add_mechanic(self):
        name = input("What's the new mechanic's name?: ")
        self.mechanics.append(Mechanic(name))

    def meet_team(self):
        for mechanic in self.mechanics:
            mechanic.greet()

    def add_car(self):
        if input("Is the car a supercar? (y/n): ") == "y":
            model = input("What model is the car?: ")
            self.cars.append(Supercar(model))
        else:
            model = input("What model is the car?: ")
            self.cars.append(Car(model))

    def check_cars(self):
        pass

    def fix_car(self):
        if self.cars:
            pass
        car = choice(self.cars)
        mechanic = choice(self.mechanic)
        car.repaired = True
        mechanic.cars_fixed += 1
        print(f"{mechanic.name} fixed the {car.model}! :)")

# def test_drive(self):
#     car = choice(self.cars)
#     if car.repaired:
#         print(f"Test driving {car.model}!")
#     else:
#         print(f"{car.model} needs to be fixed first!")

if __name__ == "__main__":
    garage = Garage()
    garage.meet_team()
    garage.asdf()
