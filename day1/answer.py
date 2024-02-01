import re

"""
    Not super proud of the part 2 solution due to the many nested for() loops.
"""

filename = "input/adv0.1.0.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def part1():
    total = 0
    for line in input:
        line = re.sub('\D', '', line)       # remove non-digits from string
        nums = int(line[0] + line[-1])      # retain only first and last digit, convert to integer
        total += nums                       # add to running total
    return total

def part2():
    values = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }
    pairs = []
    for line in input:
        digits = []
        # start at the first letter and move through it letter by letter.
        # this is the only way i've found to account for overlapping words.
        # an example is "oneight", which only matches "one" when using re.findall.
        for i,c in enumerate(line):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for k in values.keys():
                    if line[i:].startswith(k):
                        digits.append(values[k])
        pairs.append(int(f"{digits[0]}{digits[-1]}"))
    
    return sum(pairs)

print("Part one:", part1())
print("Part two:", part2())
