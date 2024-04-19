
#************************************#
#   COMP CLUB Autumn Workshops 2024  #
#    Topic: Strings!                 #
#************************************#


# Something about vowels
def main():
    string = input("String to extract vowels from: ")
    
    for letter in string:
        if (isVowel(letter)):
            print(letter)

# Determine whether or not the input 'letter' is a vowel. Return 1 if it is, and 0 if it is not.
def isVowel(letter):
    #<--Your code here-->#
    return 1


#################################################
main()
