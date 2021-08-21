import datetime


with open('/Users/arek/.config/alacritty/alacritty.yml', 'r') as f:
    nextLine = ''
    while nextLine != 'normal':
        nextLine = f.readline().strip()
    while nextLine[0:5] != 'black':
        nextLine = f.readline().strip()
    black = nextLine[7:].strip()[1:8]

with open('/Users/arek/.config/alacritty/alacritty.yml', 'r') as f:
    nextLine = ''
    while nextLine != 'normal':
        nextLine = f.readline().strip()
    while nextLine[0:5] != 'white':
        nextLine = f.readline().strip()
    white = nextLine[7:].strip()[1:8]

with open('/Users/arek/.config/alacritty/alacritty.yml', 'r') as f:
    nextLine = ''
    while nextLine[0:10] != 'background':
        nextLine = f.readline().strip()
    nextLine = nextLine[11:].strip()[1:8]
    if currentTime >= time:
        if nextLine != black:
    else:
        if nextLine != white:

