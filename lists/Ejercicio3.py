def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    temporal = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temporal

    return racers
    pass

print(purple_shell(["Mario", "Bowser", "Luigi"]))