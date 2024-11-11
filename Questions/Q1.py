
def findUnitAtPositionForAscendingIntegersStartingWith(start: int, position: int):
    index: int = position - 1
    currentNumber: int = start
    currentNumberLength: int = len(str(start))
    nextPowerOfTen: int = 10 ** currentNumberLength

    while index >= currentNumberLength:
        unitsToNextPowerOfTen: int = (nextPowerOfTen - currentNumber) * currentNumberLength
        if index < unitsToNextPowerOfTen:
            currentNumber += index // currentNumberLength
            index %= currentNumberLength
        else:
            currentNumber = nextPowerOfTen
            index -= unitsToNextPowerOfTen
            currentNumberLength += 1
            nextPowerOfTen *= 10

    print(str(currentNumber)[index])


inputStart, inputPosition = map(int, input().split(" "))
findUnitAtPositionForAscendingIntegersStartingWith(inputStart, inputPosition)