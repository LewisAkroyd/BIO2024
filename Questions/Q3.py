"""
1 = A (1)
2 = B (0, 1)
3 = AB, BA, C (1, 1, 1)
4 = ABA, AC, CA D (2, 0, 1, 1)
5 = ACA, AD, BAB, BC, CB, DA, E (2, 2, 1, 1, 1)
6 = ABAB, ABC, ACB, ADA, AE, BABA, BAC, BCA, BD, CAB, CBA, DB, EA, F (5, 4, 2, 1, 1, 1)
7 = ABABA ... G (9, 5, 3, 3, 1, 1, 1)
...
75 = ABABABABABABABABABABABABABABABABABABABABABABABABAB ... ZYX (? ... ?)
"""
def getCharScore(char: chr):
    return ord(char) - ord("A") + 1


def wordGame(pattern: str):
    patternScore: int = 0

    for char in pattern:
        patternScore += getCharScore(char)

    if patternScore == 1 or patternScore == 2:
        return 1

    seqMap: dict = {1: [1], 2: [0, 1], 3: [1, 1, 1]}

    for seqN in range(3, patternScore):
        seqMap[seqN + 1] = list()

        seqNMax: int = seqN

        if seqN > 26:
            seqNMax = 26

        for n in range(seqNMax):
            seqCount: list = seqMap[seqN - n].copy()

            if n < len(seqCount):
                seqCount.pop(n)

            seqMap[seqN + 1].append(sum(seqCount))

        if seqN < 26:
            seqMap[seqN + 1].append(1)

    position: int = 0
    remainingPatternScore: int = patternScore
    prevCharScore: int = 0

    for char in pattern:
        correction: int = 1
        currentCharScore: int = getCharScore(char)
        seqCount: list = seqMap[remainingPatternScore].copy()

        if prevCharScore != 0 and prevCharScore < currentCharScore:
            seqCount.pop(prevCharScore - 1)
            correction += 1

        if currentCharScore - correction >= 0:
            position += sum(seqCount[:currentCharScore - correction])

        remainingPatternScore -= currentCharScore
        prevCharScore = currentCharScore

    return position + 1


print(wordGame(input()))