def checkPassword(str):
    #return True if password passes
    rangeTuple, character, password = parseString(str)
    occurence = password.count(character)
    if occurence <= rangeTuple[1] and occurence >= rangeTuple[0]:
        return True
    else:
        return False

def parseString(str):
    #return char number range, password and the character to check
    ranges, iterFirst = str.split(" ", 1)
    rangeFirst, rangeSecond = ranges.split("-", 1)
    rangeTuple = (int(rangeFirst), int(rangeSecond))
    character = iterFirst[0]
    _, password = iterFirst.split(" ", 1)

    return rangeTuple, character, password

def solvePassword(fileName):
    #read input file and solve the password
    file = open(fileName, 'r')
    lines = file.readlines()

    count = 0

    for line in lines:
        if checkPassword(line):
            count += 1

    return count

print( solvePassword('inputFile'))