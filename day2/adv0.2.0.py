#adv0.2.0.py
def file_open(filename):
    # Open the file
    with open(filename) as file:
        # Read the file
        file_contents = file.readlines()
        # Format the file
        formatted_file_contents = []
        for line in file_contents:
            formatted_file_contents.append(line[:-1:])
        # Close the file
        file.close()
        # Print the file
        return formatted_file_contents

class Round:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green
    
    def __str__(self):
        return f"Red: {self.red}, Blue: {self.blue}, Green: {self.green}"
    
    

class Game:
    def __init__(self, round1, round2, round3, number):
        self.round1 = round1
        self.round2 = round2
        self.round3 = round3
        self.number = number
    
    def __str__(self):
        return f"Game: {self.number}\t Round 1: {self.round1}\t Round 2: {self.round2}\t Round 3: {self.round3}"
    
def roundProcessor(list):
    blue = 0
    if not "blue" in list:
        blue = 0
    if not "red" in list:
        red = 0
    if not "green" in list:
        green = 0
    for element in list:
        if element.isnumeric():
            if list[list.index(element) + 1] == "blue":
                blue = element
            if list[list.index(element) + 1] == "red":
                red = element
            if list[list.index(element) + 1] == "green":
                green = element
    return Round(red, blue, green)
    
def main():
    # Open the file
    file_contents = file_open("testcases/test0.2.0.txt")
    listofgames = []
    for line in file_contents:
        splitlines = line.split(":")
        gameline = splitlines[0].split(" ")
        gamenumber = int(gameline[1])
        splitlines = splitlines[1].split(";")
        roundsinfo = []
        rounds = []
        for line in splitlines:
            roundsinfo.append(line.strip().replace(",", '').split(" "))
        for round in roundsinfo:
            rounds.append(roundProcessor(round))
    #     print(rounds)
    #     listofgames.append(Game(Round(blue[2], red[2], green[2]), Round(blue[1], red[1], green[1]), Round(blue[0], red[0], green[0]), gamenumber))
    # print(listofgames[0])
    
    # # Create the game
    # game = Game(file_contents[0], file_contents[1], file_contents[2], file_contents[3])
    # # Print the game
    # print(game.round1.red)
    # print(game.round1.blue)
    # print(game.round1.green)
    # print(game.round2.red)
    # print(game.round2.blue)
    # print(game.round2.green)
    # print(game.round3.red)
    # print(game.round3.blue)
    # print(game.round3.green)
    # print(game.number)

main()