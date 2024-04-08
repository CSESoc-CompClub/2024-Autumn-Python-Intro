#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: if/else!                 #
#************************************#
import random

def main():
    number = random.randint(1,20)
    while(guess_the_number(number)):
        continue
    print("You got it! The number was", number)

def guess_the_number(number):
    n = int(input("Your guess: "))
    if (number == n): 
        return 0
    if (number < n):
        print("Too high!")
        return 1
    print("Too low!")
    return 1



#################################################
main()
