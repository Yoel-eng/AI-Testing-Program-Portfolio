import random

def listToString(list):
    finalString = ""
    for i in range(len(list)-1):
        finalString += list[i][0] 
        finalString += "|9k8fsd5|"
        for j in range(1, len(list[i])):
            for k in range(len(list[i][j])):
                for l in range(len(list[i][j][k])):
                    finalString += list[i][j][k][l]
                    if l == 0:
                        finalString += "|87xdg0|"
                if k < len(list[i][j])-1:
                    finalString += "|8s98etl|"
        finalString += "|3f2a1c4e|"
    finalString+= list[len(list)-1]
    return finalString

def stringToList(stringToConvert):
    stringToConvert = stringToConvert.split("|3f2a1c4e|")
    # If the delimiter was missing we get a list of length 1 that repeats the original
    if len(stringToConvert) == 1:
        return "|E8572.sdgfu8SD+,e3834W|" # flag = “wrong key / malformed data”
    for i in range(len(stringToConvert)):
        stringToConvert[i] = stringToConvert[i].split("|9k8fsd5|")
    for i in range(len(stringToConvert)-1):
        stringToConvert[i][1] = stringToConvert[i][1].split("|8s98etl|")
    for i in range(len(stringToConvert)-1):
        for j in range(len(stringToConvert[i][1])):
            stringToConvert[i][1][j] = stringToConvert[i][1][j].split("|87xdg0|")
    stringToConvert[len(stringToConvert)-1] = 'learn' if stringToConvert[len(stringToConvert) - 1][0] == 'learn' else 'test'
    return stringToConvert
