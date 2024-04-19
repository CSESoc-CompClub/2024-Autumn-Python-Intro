
#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: if/else!                 #
#************************************#

def main():
    year = int(input("Insert year: "))
    print(year, is_leap_year(year))

# Write a program that determines if the user's input is a leap year,
# using the following ruleset:
# If the year is a multiple of 4, it is a leap year.
# Except for every 100 years, when it is not.
# But every 400 years, it actually is again!
#
# If the year is a leap year, return the string "Is a leap year!"
# Otherwise, return the string "Is not a leap year!"
def is_leap_year(year):
    #<--Your code here-->#
    return "Is not a leap year!"

#################################################
main()
