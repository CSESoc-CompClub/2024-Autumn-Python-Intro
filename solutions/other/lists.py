import random

def main():
    my_list = []

    for i in range(1, 100):
        my_list.append(random.randint(0, 1000))

    print(my_list)


### TODO: Determine the smallest, highest and median element in the list!
    my_list.sort()
    print("MIN:")
    print(my_list[0])
    print("MAX:")
    print(my_list[-1])
    print("MEDIAN:")
    print(my_list[len(my_list)//2])

###################
main()
