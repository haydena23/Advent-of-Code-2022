# Tony Hayden
# Advent of Code 2022
# 12/13/22
# Challenge: Day 2, Part 1

overallScore = 0

# Assign each outcome a score
win = 6
tie = 3
loss = 0

# Assign each move a score
rock = 1
paper = 2
scissors = 3

# List the possible game combinations as well as their result
outcomes = [
    (rock, rock, tie),
    (rock, paper, win),
    (rock, scissors, loss),
    (paper, rock, loss),
    (paper, paper, tie),
    (paper, scissors, win),
    (scissors, rock, win),
    (scissors, paper, loss),
    (scissors, scissors, tie)
]

# Take in a game, match that to a possible outcome, and add up the game score and move score and return
def calcWin(outcome):
    matchingResult = [item for item in outcomes if item[0] == outcome[0] and item[1] == outcome[1]]
    return (matchingResult[0][1] + matchingResult[0][2])

# Open up our file, read and store every line
f = open('input.txt','r')
moves = f.read().splitlines()
f.close()

# Split each game up into the respective moves i.e ['move','move']
split = [i.split() for i in moves]

# For every single game, replace the string of the move with the point value of the move and store
replaced = []
for move in split:
    move = list(map(lambda x:rock if x == 'A' or x == 'X' else x, move))
    move = list(map(lambda x:paper if x == 'B' or x == 'Y' else x, move))
    move = list(map(lambda x:scissors if x == 'C' or x == 'Z' else x, move))
    replaced.append(move)

# In the new list of all games with all point values, calcuate the game score and add to total
for game in replaced:
    overallScore += calcWin(game)

# Print our total score of 9241
print(overallScore)