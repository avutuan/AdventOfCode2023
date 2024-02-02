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
    
    

class Game:
    def __init__(self, round1, round2, round3, number):
        self.round1 = Round(round1)
        self.round2 = Round(round2)
        self.round3 = Round(round3)
        self.number = number
        