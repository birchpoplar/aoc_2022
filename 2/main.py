# AOC 2022
# Day 2
# Part 1

pick = 0
score = 0
totalScore = 0

handle = open('input.txt', 'r')
lines = handle.readlines()

oppPicks = ['A', 'B', 'C']
slfPicks = ['X', 'Y', 'Z']

for line in lines:
    line = line.strip()
    opp, slf = line.split(' ')
    # Score for self pick
    pick = oppPicks.index(opp) + 1
    # Score for outcome
    if oppPicks.index(opp) == slfPicks.index(slf):
        score = 3
    elif slfPicks.index(slf) == (oppPicks.index(opp)+1)%3:
        score = 6
    else:
        score = 0
    totalScore += (score + pick)
    pick = score = 0

print("Total score is then " + str(totalScore))
