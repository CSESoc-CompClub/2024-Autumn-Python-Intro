
#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: Variables!               #
#************************************#

PI = 3.14159265359

# TODO: make a good intro/description for this
def main():
    ice_cream_volume()

def ice_cream_volume():
    print("<insert something about ice cream>.")
    print("The ice cream can hold", "%.2f" % ice_cream_volume(), "square centimeters of ice cream!")

# TODO: make a good intro/description for this. Something about ice cream? lol
# Students to complete the 'return' part.
def ice_cream_volume():
    radius = float(input("Radius of the cone = "))
    height = float(input("Height of the cone = "))
    # print(PI * (radius ** 2) * height / 3)
    return PI * (radius ** 2) * height / 3

#################################################
main()
