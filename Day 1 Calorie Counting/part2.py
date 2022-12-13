# Tony Hayden
# Advent of Code 2022
# 12/12/22
# Challenge: Day 1, Part 2
###########################
# Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?
###########################
import itertools

# Open the input file
filename = 'input.txt'
f = open(filename,'r')

# Declare a list to hold all of the inputs
cals = []

# Iterate through every line of the input file and add to cals
for line in f:
    if line == '\n':
        cals.append(line + '\n') # Add extra \n on line breaks for delimiter
    else:
        cals.append(line)

# Delimiter is '\n\n' since it only occurs in between groups
delimiter = '\n\n'

# Create a list of subgroups split up by the delimiter
split = [list(y) for x, y in itertools.groupby(cals, lambda z: z == delimiter) if not x]

# Cast all of the numbers in the subgroups from str to int
split = [[int(y) for y in x] for x in split]

# Calculate the sum for each of the subgroups
sums = list(map(sum, split))

# Calculate and print the top three total
print(sum(sorted(sums, key = lambda x: x, reverse = True)[:3]))

# Answer: 197291 calories