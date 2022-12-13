import itertools

filename = 'input.txt'
f = open(filename,'r')
cals = []

for line in f:
    if line == '\n':
        cals.append(line + '\n')
    else:
        cals.append(line)

delimiter = '\n\n'

split = [list(y) for x, y in itertools.groupby(cals, lambda z: z == delimiter) if not x]
split = [[int(y) for y in x] for x in split]

