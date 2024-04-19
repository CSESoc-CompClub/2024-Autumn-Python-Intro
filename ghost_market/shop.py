from constants import CATALOGUE, is_valid_item, get_price

"""
Add, remove, and show items in our customer's shopping cart.

This is your second task of the project.
"""


def add_to_cart(cart):
    """
    'cart' is a list of all the items in our customer's cart

    Prompt the customer for an item to buy:
    -> if it exists in our catalogue, add it to the customer's cart
    -> otherwise, let the customer know this item does not exist

    HINT: You can use the is_valid_item(item) from constants.py to check if the item exists in the catalogue
    """
    # TODO: COMPLETE ME

    return cart


def remove_from_cart(cart):
    """
    'cart' is a list of all the items in our customer's cart

    Prompt the customer for an item to remove:
    -> if it exists in our cart, remove 1 of it
    -> otherwise, let the customer know this item does not exist
    """
    # TODO: COMPLETE ME

    return cart


def show_items(cart):
    """
    'cart' is a list of all the items in our customer's cart
    loop through our list and print them out in the following format:

    Your Cart: Omamori, Onigiri, Omamori, Aji Fry

    Hint: We can start off with an empty string, and just append the next item to it :)
     """
    # TODO: COMPLETE ME