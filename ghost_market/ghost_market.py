"""Ghost market shopping spree!!"""

# You do not need to modify this file, though you are certainly
# welcome to read through it. We hope you enjoy and learn a lot
# from working on this project.
# 	The CompClub Team

from constants import list_to_dict
from welcome import welcome, get_next_customer, display_catalogue
from shop import add_to_cart, remove_from_cart, show_items
from checkout import checkout

def main():
    welcome()
    customer = get_next_customer()
    cart = []  # list of item names

    while True:
        display_catalogue()

        # Interpret EOF as quit.
        try:
            while True:
                command = input("\nEnter a command: ")
                if command.strip() != "":
                    break
        except EOFError:
            break

        if command in ("q", "quit"):
            break

        elif command in ("b", "buy"):
            cart = add_to_cart(cart)

        elif command in ("r", "remove"):
            cart = remove_from_cart(cart)

        elif command in ("s", "show"):
            show_items(cart)

        elif command in ("c", "checkout"):
            checkout(customer, list_to_dict(cart))
            customer = get_next_customer()
            cart = {}

        else:
            print(
                "There are a few commands to learn:\n"
                "		q, quit - Close the market\n"
                "		b, buy - Add an item to cart\n"
                "		r, remove - Remove an item from cart\n"
                "		c, checkout - Finalise and checkout your order!\n"
            )

main()