spam_amount = 0
type (spam_amount)
type(19.95)

print('Order of operations')
print(5 / 2)
print(6 / 2)
print('------')
print(5 // 2)
print(6 // 2)
print('------')
print(8 -3 + 2)
print(-3 + 4 * 2)

print("\nSometimes the default order of operations isn't what we want:")
hat_height_cm = 25
my_height_cm = 190

total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

print('\nmin and max return the minimum and maximum of their arguments')
print(min(1, 2, 3))
print(max(1, 2, 3))

print('\nabs returns the absolute value of an argument')
print(abs(32))
print(abs(-32))

print('\nnumerical types, int and float')
print(float(10))
print(int(3.33))

print(int('807') + 1)