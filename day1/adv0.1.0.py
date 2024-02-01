#adv0.1.0.py
import re

def readfile(file):
##    input: filename/path
##    output: list of lines formatted
    # initialize empty list for output named lines
    lines = []
    # sets open file to simply variable "f"
    with open(file, 'r') as f:
        for line in f:
            # appends every line of the file to lines without "\n"
            lines.append(line[:-1:])
    # returns output, lines
    return lines

def calvalwithdig(line):
##    input: string
##    output: value (integer)
    # using regex to make a list, nums, of all digits in the string
    nums = re.findall(r'\d', line)
    # if there's only one digit in the string
    if len(nums) == 1:
        # the value is that single digit twice
        value = int(str(nums[0]) + str(nums[0]))
    # if there's more than one digit in the string
    elif len(nums) > 1:
        # the value is the first and last index of nums
        value = int(str(nums[0]) + str(nums[-1]))
    # if there's no digits in the string
    else:
        # the value is 0
        value = 0
    # returns output, value
    return value

def convert(number):
    word_dig = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    if number in word_dig.keys():
        return word_dig[number]  
    else:
        return str(number)
    
def calvalwithword(line):
    nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    for ele in nums:
        num = convert(ele)
        new = ele[0] + num + ele[-1]
        line = re.sub(ele, new, line)
    nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    if len(nums) == 1:
        value = int(str(convert(nums[0])) + str(convert(nums[0])))
    elif len(nums) > 1:
        value = int(str(convert(nums[0])) + str(convert(nums[-1])))
    else:
        value = 0
    return value


if __name__ == "__main__":
    value = 0
    lines = readfile("input/adv0.1.0.txt")
    for line in lines:
        value += calvalwithword(line)
    print('answer:', value)
