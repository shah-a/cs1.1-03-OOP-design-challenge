from random import choice

from cars import Car, Supercar
from mechanic import Mechanic

class Garage:
    """
    Class for Garage.

    Access modifier rationale:
    self.__cars and self.__mechanics are both private attributes;
    They are not used anywhere in the program outside of the garage class.
    Users can access the data by calling the appropriate methods.
    """

    def __init__(self):
        self.__cars = []
        self.__mechanics = [Mechanic("Jerry")]  # Instantiate Mechanic

    def meet_team(self):
        for mechanic in self.__mechanics:
            mechanic.greet()
        print(f"\nOur shop uses {Mechanic.uniform_colour} uniforms!")

    def change_uniform(self):
        colour = input("What's the new colour?: ")
        Mechanic.change_uniform(colour)

    def add_mechanic(self):
        name = input("What's the new mechanic's name?: ")
        self.__mechanics.append(Mechanic(name))  # Instantiate Mechanic

    def add_car(self):
        if input("Is the car a supercar? (y/n): ") == "y":
            model = input("What model is the car?: ")
            self.__cars.append(Supercar(model))  # Instantiate Supercar
        else:
            model = input("What model is the car?: ")
            self.__cars.append(Car(model))  # Instantiate Car

    def check_cars(self):
        if self.__cars:
            for car in self.__cars:
                car.check_status()
        else:
            print("Currently no cars in the garage!")

    def fix_car(self):
        if self.__cars:
            # Makes a list of cars in self.__cars that need to be fixed
            cars = [car for car in self.__cars if car.repaired == False]
            if cars:
                car_to_fix = choice(cars)
                choice(self.__mechanics).fix_car(car_to_fix)
            else:
                print("No cars need fixing :) yay!")
        else:
            print("Currently no cars in the garage!")

    def test_drive(self):
        if self.__cars:
            # Makes a list of cars in self.__cars that need to be fixed
            cars = [car for car in self.__cars if car.repaired == True]
            if cars:
                choice(cars).test_drive()
            else:
                print("Cars need to be fixed first!")
        else:
            print("Currently no cars in the garage!")

    def burnout(self):
        if self.__cars:
            # Makes a list of supercar instances in self.__cars
            supercars = [car for car in self.__cars if isinstance(car, Supercar)]
            if supercars:
                fixed_supercars = [car for car in supercars if car.repaired == True]
                if fixed_supercars:
                    choice(supercars).burnout()
                else:
                    print("Supercars need to be fixed first!")
            else:
                print("Currently no super cars in the garage!")
        else:
            print("Currently no cars in the garage!")
