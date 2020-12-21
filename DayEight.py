from os import access


with open('bootcode.txt') as file:
    BootCode = file.readlines()
    BootCode = [line.strip() for line in BootCode]

startingInstruction = BootCode[0]
startingIndex = 0
uniqueInstructions = []
accumulator = 0

# Recursive Function


def executeInstruction(line, index):
    global accumulator
    currentIndex = index
    line = line.split(' ')
    instType = line[0]
    instIncrement = line[1]
    incrementAmount = int(instIncrement[1:])
    incrementSymbol = instIncrement[0]

    if instType == 'acc':
        if currentIndex not in uniqueInstructions:
            uniqueInstructions.append(currentIndex)
            nextIndex = currentIndex + 1
            if incrementSymbol == '+':
                accumulator += incrementAmount
            if incrementSymbol == '-':
                accumulator -= incrementAmount
            executeInstruction(BootCode[index + 1], nextIndex)

        if currentIndex in uniqueInstructions:
            return accumulator

    elif instType == 'jmp':
        nextIndex = currentIndex
        if incrementSymbol == '+':
            nextIndex = currentIndex + incrementAmount
        if incrementSymbol == '-':
            nextIndex = currentIndex - incrementAmount
        if currentIndex not in uniqueInstructions:
            uniqueInstructions.append(currentIndex)
            executeInstruction(BootCode[nextIndex], nextIndex)
        if currentIndex in uniqueInstructions:
            return accumulator

    elif instType == 'nop':
        if currentIndex not in uniqueInstructions:
            nextIndex = currentIndex + 1
            executeInstruction(BootCode[nextIndex], nextIndex)
        if currentIndex in uniqueInstructions:
            return accumulator


accValue = executeInstruction(startingInstruction, startingIndex)
print(accValue)
