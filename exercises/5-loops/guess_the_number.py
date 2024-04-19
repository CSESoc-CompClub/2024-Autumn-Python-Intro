#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: if/else!                 #
#************************************#
import random

def main():
    number = random.randint(1,20)
    while(not guess_the_number(number)):
        continue
    print("You got it! The number was", number)

# Write a program that returns 1 if the user inputs the correct number,
# and returns 0 if the number was too high or too low.
# You should also tell the user if their input was too high or too low,
# by checking how the value of 'number' compares to their input 'n'
def guess_the_number(number):
    n = int(input("Your guess: "))
    #<--Your code here-->#
    return 0




#################################################
main()
