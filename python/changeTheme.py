import yaml
import datetime

def getYamlContents(path: str):
    with open(path, 'r') as f:
        try:
            contents = yaml.safe_load(f)
            return contents
        except yaml.YAMLError as e:
            print(e)

def changeTheme(toTheme, contents):

    if toTheme == "dark":
        newBgColor = contents['colors']['normal']['black']
    elif toTheme == "light":
        newBgColor = contents['colors']['normal']['white']

    if contents['colors']['primary']['background'] != newBgColor:
            contents['colors']['primary']['background'] = newBgColor
    return contents

def decideTheme():
    now = datetime.datetime.today()
    time = now.time()
    eighteen = datetime.time(18)
    if time < eighteen:
        toTheme = "light"
    else:
        toTheme = "dark"
    return toTheme

def putYamlContents(contents, path):
    with open(path, 'w') as f:
        yaml.dump(contents, f)
