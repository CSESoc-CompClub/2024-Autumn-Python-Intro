CATALOGUE = {
    "Food": {
        "Konpeito": 0.5,
        "Herring and Pumpkin Pie": 20,
        "Nabeyaki Udon": 12,
        "Haku's Onigiri": 5,
        "Howl's Bacon and Eggs": 10,
        "Aji Fry": 8.5,
        "Kiki's Chocolate Cake": 17,
    },
    "Trinkets": {
        "Bamboo Fan": 10,
        "Omamori": 2,
        "Bright red bow": 5,
        "Teardrop earrings": 12,
        "Sturdy Umbrella": 15.5,
    },
}


# Returns True if the Item exists in the Catalogue
# Returns False otherwise
def is_valid_item(item):
    for category in CATALOGUE:
        if item in CATALOGUE[category]:
            return True
    return False


# Returns the price of the item if it exists in the Catalogue
# Returns None otherwise
def get_price(item):
    for category in CATALOGUE:
        if item in CATALOGUE[category]:
            return CATALOGUE[category][item]
    return None


def list_to_dict(list):
    res = {}
    for item in list:
        if item in res:
            res[item] += 1
        else:
            res[item] = 1
    
    return res