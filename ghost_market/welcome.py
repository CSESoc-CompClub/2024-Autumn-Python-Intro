"""
Open your stall with a welcome message, 
and get your customer's name!

This is your first task of the project.
"""
from constants import CATALOGUE

def welcome():
    """Print a warming welcome message!"""
    # TODO: Write your code here
    pass


def get_next_customer() -> str:
    """Prompt the customer for their name, and return it"""
    # TODO: Write your code here
    return "NAME HERE"
    

def display_catalogue():
    print(f"Here's what we have on the catalogue tonight:")
    for category, items in CATALOGUE.items():
        print(f"\n====={category.upper()}=====")
        for name, price in items.items():
            print(f"{name:<30}${price}")
    
