#
# //============================//
# //  Guessing Game Gone Wrong  //
# //============================//
#
# I've coded up a guessing game but my friend keeps telling me that they've
# tried every single number and haven't been able to get it
# I'm looking at my code and I feel like it looks correct.
# Where exactly did I go wrong? My other friend tells me I have 2 main mistakes

hidden_number = 10
guess = input("What do you guess my hidden number is? ")
while guess != hidden_number:
    print("Your guess is incorrect. Try again :(")
    input("Try guess my hidden number again. What do you think it is? ")
