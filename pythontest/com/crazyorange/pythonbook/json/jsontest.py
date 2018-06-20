import json

inputname = input('please input your name :')
path = '/Users/apple/Desktop/Exercise/Exercise/pythontest/com/crazyorange/test.json'


def getUserName(name):
    saveName = ''
    if name is not None:
        try:
            with open(path, 'w') as file:
                json.dump(name, file)
                print('We will remember this name : ' + name)
        except FileNotFoundError:
            print('file is not found')
        else:
            with open(path, 'r') as file:
                saveName = json.load(file)

    return saveName
