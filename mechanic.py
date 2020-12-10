class Mechanic:
    """
    Class for Mechanic.

    Access modifier rationale:
    Class attribute uniform_colour is public to allow access in garage module.
    Instance attributes are private; data can be accessed with methods in Garage class
    """

    uniform_colour = "blue"

    def __init__(self, name):
        self.__name = name
        self.__cars_fixed = 0

    def greet(self):
        print(f"I'm {self.__name}! I've fixed {self.__cars_fixed} cars.")

    def fix_car(self, car):
        car.repaired = True
        self.__cars_fixed += 1
        print(f"{self.__name} fixed the {car.model}! :)")

    @classmethod
    def change_uniform(cls, colour):
        cls.uniform_colour = colour
