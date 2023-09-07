primes = [2, 3, 5, 7]
print(primes)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
print(hands)

my_favourite_things = [32, 'raindrops on roses', help]
print(my_favourite_things)
# (Yes, Python's help function is *definitely* one of my favourite things)

############################
print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[-2])

############################
print(planets[0:3])
print(planets[:3])
print(planets[3:])

############################
print(planets[1:-1])
print(planets[-3:])

############################
planets[3] = 'Malacandra'

############################
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

############################
# How many planets are there?
print(len(planets))

############################
# The planets sorted in alphabetical order
print(sorted(planets))

primes = [2, 3, 5, 7]
print(sum(primes))
print(max(primes))

############################
x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

############################
print(x.bit_length)
print(x.bit_length())

############################
help(x.bit_length)

############################
# Pluto is a planet darn it!
planets.append('Pluto')
help(planets.append)
print(planets)
print(planets.pop())
print(planets)
print(planets.index('Earth'))

############################
print('Earth' in planets)
print('Calbefraques' in planets)
help(planets)

############################
t = (1, 2, 3)
print(t)

############################
x = 0.125
print(x.as_integer_ratio())
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)