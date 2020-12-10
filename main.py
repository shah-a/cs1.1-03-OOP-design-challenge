# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Dec. 05, 2020

"""CS1.1 Assignment 3: OOP Design Challenge."""

from garage import Garage

# Instantiate Garage
garage = Garage()

# Initiate menu loop
menu = None

print("----------------------------------------")
print("Welcome to Jerry's Auto Garage!")

while menu != "0":
    print("----------------------------------------")
    menu = input(
        "[0] Exit\n\n"
        "[1] Meet Team\n"
        "[2] Change Uniform\n"
        "[3] Add Mechanic\n\n"
        "[4] Add Car\n"
        "[5] Check Cars\n"
        "[6] Fix Car\n\n"
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
    elif menu == "0":
        print("Bye! Take care :)")
        print("----------------------------------------")
