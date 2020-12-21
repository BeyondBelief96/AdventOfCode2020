PasswordData = []
PasswordData = open("./Passwords.txt", "r").readlines()
Passwords = []
Policies = []

targetCharacters = []


def ReadFile():
    for line in PasswordData:
        data = line.split(' ')
        if line != '\n':
            Passwords.append(data[2].rstrip('\n'))
            Policies.append(data[0])
            targetCharacters.append(data[1].rstrip(':'))


def ProcessData():
    characterIndex = 0
    answerCount = 0
    for policy in Policies:
        bothNums = policy.split('-')
        firstNum: int = int(bothNums[0])
        secondNum: int = int(bothNums[1])
        password = Passwords[characterIndex]

        firstIndexMatch = password[firstNum -
                                   1] == targetCharacters[characterIndex]
        secondIndexMatch = password[secondNum -
                                    1] == targetCharacters[characterIndex]

        if firstIndexMatch and secondIndexMatch:
            answerCount += 0
        if firstIndexMatch and not secondIndexMatch:
            answerCount += 1
        if secondIndexMatch and not firstIndexMatch:
            answerCount += 1
        characterIndex += 1
    print(f"We have {answerCount} valid passwords.")


if __name__ == '__main__':
    ReadFile()
    ProcessData()
