def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    #return (int(ketchup) + int(mustard) + int(onion)) == 1
    return (ketchup + mustard + onion) == 1
    pass

print(exactly_one_topping(1,0,0))