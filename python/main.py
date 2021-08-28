import argparse
import changeTheme

def main():

    parser = argparse.ArgumentParser(description='Change Alacritty Theme.')
    parser.add_argument('path')

    args = parser.parse_args()
    path = args.path
    contents = changeTheme.getYamlContents(path)
    toTheme = changeTheme.decideTheme()
    print(toTheme)
    newContents = changeTheme.changeTheme(toTheme, contents)
    changeTheme.putYamlContents(newContents, path)

if __name__ == "__main__":
    main()
