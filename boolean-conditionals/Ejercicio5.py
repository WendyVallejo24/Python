# a
def onionless(onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion
print(onionless(onion=False))

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion
    pass

print(wants_all_toppings(ketchup=False, mustard=True, onion=False))

print("...............")
#b
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)
    pass

print(wants_plain_hotdog(ketchup=False, mustard=False, onion=False))

print("...........")
#c
def exactly_one_sauce(ketchup, mustard):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)
    pass
print(exactly_one_sauce(ketchup=True, mustard=False))