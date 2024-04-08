
#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: Variables!               #
#************************************#

PI = 3.14159265359

# TODO: make a good intro/description for this
def main():
    print("-==Variables 1==-")
    exercise_one()

    print("\n\n-==Variables 2==-")
    exercise_two()


def exercise_one():
    print(
""" -==Dish Menu==-
1. Onigiri (200 cal)
2. Red bean buns (250 cal)
3. Sponge cake (500 cal)
4. Okayu (650 cal)
5. Ramen (800 cal)
"""
        )
    calories = handle_user_input()
    print("That will be", calories, "calories!")

# Students to complete the 'return' part.
def handle_user_input():
    energy = [200, 250, 500, 650, 800]
    dish = int(input("Enter dish (1-5) that you would like to have: "))
    amount = int(input("How much of this dish would you like to have: "))
    return amount * energy[dish - 1]


def exercise_two():
    print("<insert something about ice cream>.")
    print("The ice cream can hold", "%.2f" % ice_cream_volume(), "square centimeters of ice cream!")



# TODO: make a good intro/description for this. Something about ice cream? lol
# Students to complete the 'return' part.
def ice_cream_volume():
    radius = float(input("Radius of the cone = "))
    height = float(input("Height of the cone = "))
    return PI * (radius ** 2) * height / 3

#################################################
main()
