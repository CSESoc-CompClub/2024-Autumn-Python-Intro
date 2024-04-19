"""
Checkout our order!

This is your third task of the project. A useful function from constants.py has been imported for you, if you
want to use other functions you can import them in a similar manner.
An example cart and customer have been given to you to test the functions. Scroll to the bottom to see expected output.
"""

from constants import get_price

example_cart = {"Konpeito": 3, "Aji Fry": 2}
example_customer = "Bob"


def checkout(name, cart):
    print("== Checkout ==")
    payment = input("Enter payment amount: ")

    cost = 0
    for item in cart:
        cost += get_price(item)

    if float(payment) < float(cost):
        print(
            "Sorry, you don't have enough money to buy all the items in your cart! :("
        )
    else:
        print_reciept(name, cart, payment)


def print_reciept(name, cart, paid_amount):
    total_cost = 0
    print("Thank you " + name + " for shopping with us! ^.^!")
    print("Reciept:")

    f = open(f"{name}.txt", "a")
    f.write("")
    for item in cart:
        item_details = item + " x" + str(cart[item])
        cost = get_price(item)
        line = "{0:20}  ${1}".format(item_details, cost)
        f.write(line + "\n")
        print(line)
        total_cost += float(cost)

    f.write("\n{0:20}  ${1}\n".format("TOTAL", total_cost))
    f.write("{0:20}  ${1}\n".format("PAID", paid_amount))
    print("\n{0:20}  ${1}".format("TOTAL", total_cost))
    print("{0:20}  ${1}".format("PAID", paid_amount))

    change = float(paid_amount) - float(total_cost)
    f.write("{0:20}  ${1}".format("CHANGE", change))
    print("{0:20}  ${1}".format("CHANGE", change))
