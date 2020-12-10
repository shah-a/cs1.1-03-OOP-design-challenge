class Mechanic:
    """
    Class for Mechanic.

    Access modifier rationale:
    All attributes are public to allow access in the garage module.
    """

    uniform_colour = "blue"

    def __init__(self, name):
        self.name = name
        self.cars_fixed = 0

    def greet(self):
        print(f"I'm {self.name}! I've fixed {self.cars_fixed} cars.")

    def fix_car(self, car):
        car.repaired = True
        self.cars_fixed += 1
        print(f"{self.name} fixed the {car.model}! :)")

    @classmethod
    def change_uniform(cls, colour):
        cls.uniform_colour = colour
