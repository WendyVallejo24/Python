party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford', 'Gina']

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1

print(fashionably_late(sorted(party_attendees), 'May'))