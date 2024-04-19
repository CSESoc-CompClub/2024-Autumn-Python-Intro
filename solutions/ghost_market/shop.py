from constants import CATALOGUE, is_valid_item, get_price

"""
Add, remove, and show items in our customer's shopping cart.

This is your second task of the project.
"""


def add_to_cart(cart):
    """
    Prompt the customer for an item to buy:
    -> if it exists in our catalogue, add it to the customer's cart
    -> otherwise, let the customer know this item does not exist

    HINT: You can use the is_valid_item(item) from constants.py to check if the item exists in the catalogue
    """

    # <SOLUTION>:
    item = input("What would you like to buy? ")
    if is_valid_item(item):
        cart.append(item)
        print("Added 1", item, "to cart.")
    else:
        print("Sorry, we do not have that item.")
    # </SOLUTION>:

    return cart


def remove_from_cart(cart):
    """
    Prompt the customer for an item to remove:
    -> if it exists in our cart, remove 1 of it
    -> otherwise, let the customer know this item does not exist
    """

    # <SOLUTION>:
    item = input("What would you like to remove? ")
    if item in cart:
        cart.remove(item)
        print("Removed 1", item, "removed from cart.")
    else:
        print("Sorry, you do not have that item in your cart.")
    # </SOLUTION>:

    return cart


def show_items(cart):
    """
    Display the names and quantities of items that the customer
    has added to their cart. Also sum up the current total and print it.

    Try get this format:
    Your Cart:
    QUANTITY    ITEM
    1           Konpeito
    2           Herring and Pumpkin Pie
    1           Nabeyaki Udon
    1           Haku's Onigiri
    1           Howl's Bacon and Eggs

    Total: $ 67.5

    HINT: Try use "\t" in your print statements to make it look nice
    HINT: You can use the get_price() function from constants.py to get the price of an item
    """

    # <SOLUTION>:
    total = 0
    print("Your cart:")
    print("QUANTITY \t ITEM")
    for item in cart:
        print(cart[item], "\t\t", item)
        total += get_price(item) * cart[item]
    print("\nTotal: $", total)
    # </SOLUTION>:

    pass