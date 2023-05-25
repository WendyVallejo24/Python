def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False

print(menu_is_boring(['bacon', 'eggs', 'milk', 'juice', 'rice', 'eggs', 'eggs']))