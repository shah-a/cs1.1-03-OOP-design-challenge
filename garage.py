# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Dec. 05, 2020

"""CS1.1 Assignment 3: OOP Design Challenge."""

from random import choice

from cars import Car, Supercar
from mechanic import Mechanic

class Garage:
    def __init__(self):
        self.cars = []
        self.mechanics = [Mechanic("Jerry")]

    def meet_team(self):
        for mechanic in self.mechanics:
            mechanic.greet()
        print(f"\nOur shop uses {Mechanic.uniform_colour} uniforms!")

    def change_uniform(self):
        colour = input("What's the new colour?: ")
        Mechanic.uniform_colour = colour

    def add_mechanic(self):
        name = input("What's the new mechanic's name?: ")
        self.mechanics.append(Mechanic(name))

    def add_car(self):
        if input("Is the car a supercar? (y/n): ") == "y":
            model = input("What model is the car?: ")
            self.cars.append(Supercar(model))
        else:
            model = input("What model is the car?: ")
            self.cars.append(Car(model))

    def check_cars(self):
        if self.cars:
            for car in self.cars:
                car.check_status()
        else:
            print("Currently no cars in the garage!")

    def fix_car(self):
        if self.cars:
            # Makes a list of cars in self.cars that need to be fixed
            cars = [car for car in self.cars if car.repaired == False]
            if cars:
                car_to_fix = choice(cars)
                choice(self.mechanics).fix_car(car_to_fix)
            else:
                print("No cars need fixing :) yay!")
        else:
            print("Currently no cars in the garage!")

    def test_drive(self):
        if self.cars:
            car = choice(self.cars)
            car.test_drive()
        else:
            print("Currently no cars in the garage!")

    def burnout(self):
        if self.cars:
            # Makes a list of supercar instances in self.cars
            supercars = [car for car in self.cars if isinstance(car, Supercar)]
            if supercars:
                choice(supercars).burnout()
            else:
                print("Currently no super cars in the garage!")
        else:
            print("Currently no cars in the garage!")

if __name__ == "__main__":
    garage = Garage()

    menu = None
    while menu != "0":
        print("----------------------------------------")
        menu = input(
            "\n[0] Exit\n\n"
            "[1] Meet Team\n"
            "[2] Change Uniform\n"
            "[3] Add Mechanic\n\n"
            "[4] Add Car\n"
            "[5] Check Cars\n"
            "[6] Fix Car\n"
            "[7] Test Drive\n"
            "[8] Do a burnout!!!\n\n"
            "Your choice: "
        )
        print("\n----------------------------------------")
        if menu == "1":
            garage.meet_team()
        elif menu == "2":
            garage.change_uniform()
        elif menu == "3":
            garage.add_mechanic()
        elif menu == "4":
            garage.add_car()
        elif menu == "5":
            garage.check_cars()
        elif menu == "6":
            garage.fix_car()
        elif menu == "7":
            garage.test_drive()
        elif menu == "8":
            garage.burnout()
