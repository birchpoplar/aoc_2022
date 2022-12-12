# AOC 2022
# Day 1
# Part 1

elves = []
carry = 0

handle = open('input.txt', 'r')
lines = handle.readlines()

for line in lines:
    line = line.strip()
    if line == '':
        elves.append(carry)
        carry = 0
    elif int(line) > 0:
        carry += int(line)

        
print("Counted " + str(len(elves)) + " elves carrying stuff.")
print("Max carry is " + str(max(elves)))

# Part 2

TOPC = 3
topcount = TOPC
topsum = 0

while (topcount > 0):
    print("Checking max across " + str(len(elves)) + " elves")
    topsum += max(elves)
    elves.remove(max(elves))
    topcount -= 1

print("Total calories across the top " + str(TOPC) + " elves is " + str(topsum))
