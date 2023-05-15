# Your code goes here. Define a function called 'sign'
def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
    
print(sign(4))
print(sign(-4))
print(sign(0))