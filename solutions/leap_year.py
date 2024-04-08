
#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: if/else!                 #
#************************************#

def main():
    year = int(input("Insert year: "))
    print(year, is_leap_year(year))

def is_leap_year(year):
    if (year % 400 == 0):
        return "Is a leap year!"

    if (year % 100 == 0):
        return "Is not a leap year!"

    if (year % 4 == 0):
        return "Is a leap year!"

    return "Is not a leap year!"













#################################################
main()
