import re

benchmarks = {
    'red':12,
    'green': 13,
    'blue': 14
}

games_input = None

with open("input/adv0.2.0.txt") as file:
    games_input = file.readlines()
    
answer = 0

for game in games_input:
    sets = game.split(';')
    game_id = int(''.join(re.findall(r'Game (\d+)', game)))
    colors = []
    condition = 1
    for element in sets:
        red = ''.join(re.findall(r'(\d+) red', element))
        blue = ''.join(re.findall(r'(\d+) blue', element))
        green = ''.join(re.findall(r'(\d+) green', element))
        if not red.isnumeric():
            red = '0'
        if not blue.isnumeric():
            blue = '0'
        if not green.isnumeric():
            green = '0'
        rownd = {
            'red':int(red),
            'green':int(green),
            'blue':int(blue)
        }
        colors.append(rownd)
    for element in colors:
        condition *= element['red'] <= benchmarks['red']
        condition *= element['blue'] <= benchmarks['blue']
        condition *= element['green'] <= benchmarks['green']
    if condition:
        answer += game_id
        
print(answer)
