with open("answers.txt") as file:
    answers = file.readlines()
    answers = [line.strip() for line in answers]

groups = []


def ParseData(data):
    group = []
    for line in data:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)


def FindCorrectAnswers(groupList):
    uniqueCorrectAnswers = 0
    for group in groupList:
        groupSet = set()
        for line in group:
            lineSet = set(line)
            groupSet = groupSet.union(lineSet)
        uniqueCorrectAnswers += len(groupSet)
    print(uniqueCorrectAnswers)


ParseData(answers)
FindCorrectAnswers(groups)

# PART TWO


def FindAllUniqueAnswers(data):
    answerCount = 0
    for group in data:
        uniqueAnswers = set()
        for line in group:
            for character in line:
                characterSet = set(character)
                uniqueAnswers = uniqueAnswers.union(characterSet)
        for char in uniqueAnswers:
            lineCounter = 0
            for line in group:
                if char in line:
                    lineCounter += 1
            if lineCounter == len(group):
                answerCount += 1
    print(answerCount)


FindAllUniqueAnswers(groups)
