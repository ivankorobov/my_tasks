import itertools
colors = ['red', 'white', 'blue', 'black']

for i in itertools.permutations(colors, 2):
    print(i)

print('*' * 50)

for i in itertools.combinations(colors, 2):
    print(i)

my_cycle = itertools.cycle(colors)
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))

