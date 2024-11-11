import math


def formatParseDescription(parseDescription: str):
    indentation: int = 0
    index: int = -1

    if parseDescription[index] == ")":
        parseDescription = parseDescription[:index]
        indentation += 1
        index += 1

    while indentation > 0:
        index -= 1
        if parseDescription[index] == ")":
            indentation += 1
        elif parseDescription[index] == "(":
            indentation -= 1

    if parseDescription[index] == "(":
        parseDescription = parseDescription[:index] + parseDescription[index + 1:]
        index += 1

    if parseDescription[:index] == "":
        return formatParseDescription(parseDescription[index:])
    return parseDescription[:index], parseDescription[index:]


def resolveParsedValue(parsedValue: str, position: int):
    if parsedValue == "E":
        return position * 2
    elif parsedValue == "O":
        return position * 2 - 1
    elif parsedValue == "T":
        return math.ceil((-1 + (1 + 8 * position) ** 0.5) / 2)


def resolveParseDescription(parseDescription: str, position: int):
    if len(parseDescription) == 1:
        return resolveParsedValue(parseDescription, position)
    parseDescriptionLeft, parseDescriptionRight = formatParseDescription(parseDescription)
    return resolveParseDescription(parseDescriptionRight, resolveParseDescription(parseDescriptionLeft, resolveParseDescription(parseDescriptionRight, position)))


inputStart, inputPosition = input().split(" ")
print(resolveParseDescription(inputStart, int(inputPosition)))
