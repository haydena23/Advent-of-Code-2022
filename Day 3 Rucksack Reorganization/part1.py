# Tony Hayden
# Advent of Code 2022
# 12/14/22
# Challenge: Day 3, Part 1

import string

# Define every letter their priority value
priorities = dict()
for index, letter in enumerate(string.ascii_letters):
    priorities[letter] = index + 1

# Read every rucksack and store
f = open('input.txt','r')
rucksacks = f.read().splitlines()
f.close()

# Parse every rucksack
for i in range(len(rucksacks)):
    firstHalf = rucksacks[i][:len(rucksacks[i])//2] # First half of rucksack string
    secondHalf = rucksacks[i][len(rucksacks[i])//2:] # Second half of rucksack string
    commonLetter = ''.join(set(firstHalf).intersection(set(secondHalf))) # Find common letter using set intersection
    rucksacks[i] = [[*firstHalf],[*secondHalf],commonLetter] # Store each half as a list of characters

# For each pack, add the priority value of the common letter to the running total
total = 0
for pack in rucksacks:
    total += priorities[pack[2]]

# Print running total of 7795
print(total)