def ruound_to_two_places(num):
    return(round(num, 2))
print(ruound_to_two_places(9.9999))

print("........")
x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))
print(smallest_abs)

print("........")
def f(x):
    y = abs(x)
    return y

print(f(5))