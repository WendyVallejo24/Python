def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0
    pass

print(concise_is_negative(2))
print(concise_is_negative(-10))