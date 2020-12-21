from os import closerange


with open('passports.txt') as file:
    unfilteredPassports = file.readlines()
    unfilteredPassports = [line.strip() for line in unfilteredPassports]

passports = []
passportFields = ['ecl', 'pid', 'byr', 'iyr', 'hgt', 'hcl', 'eyr']
validPassports = []


def ParseData(data):
    passportData = ''
    for line in data:
        if line != '':
            passportData += ' ' + line
        else:
            passports.append(passportData)
            passportData = ''


def isValidPassport(passport):
    for field in passportFields:
        if field not in passport:
            return False
    return True


def CheckPassports(passports):
    validPassportCount = 0
    for passport in passports:
        isPassportValid = isValidPassport(passport)
        if isPassportValid is True:
            validPassportCount += 1
            validPassports.append(passport)
    print(validPassportCount + 1)


ParseData(unfilteredPassports)
CheckPassports(passports)

# PART TWO:


def isByrValid(fieldValue):
    if 1920 <= int(fieldValue) <= 2002:
        return True
    else:
        return False


def isIyrValid(fieldValue):
    if 2010 <= int(fieldValue) <= 2020:
        return True
    else:
        return False


def isEyrValid(fieldValue):
    if 2020 <= int(fieldValue) <= 2030:
        return True
    else:
        return False


def isHgtValid(fieldValue):
    if 'cm' in fieldValue:
        fieldValue = fieldValue.replace('cm', '')
        if 150 <= int(fieldValue) <= 193:
            return True
    if 'in' in fieldValue:
        fieldValue = fieldValue.replace('in', '')
        if 59 <= int(fieldValue) <= 76:
            return True
    else:
        return False


def isHclValid(fieldValue):
    validCharacters = ['0', '1', '2', '3', '4', '5', '6',
                       '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if fieldValue[0] == '#':
        fieldValue = fieldValue.replace('#', '')
        if len(fieldValue) == 6:
            for character in fieldValue:
                if character in validCharacters:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


def isEclValid(fieldValue):
    return fieldValue in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def isPidValid(fieldValue):
    if len(fieldValue) == 9 and fieldValue.isdigit():
        return True
    else:
        return False


def hasValidData(passport):
    passport = passport.split()
    fieldData = {}

    for item in passport:
        key = item[:3]
        value = item[4:]
        fieldData[key] = value

    if not isByrValid(fieldData['byr']):
        return False
    if not isIyrValid(fieldData['iyr']):
        return False
    if not isEyrValid(fieldData['eyr']):
        return False
    if not isHgtValid(fieldData['hgt']):
        return False
    if not isHclValid(fieldData['hcl']):
        return False
    if not isEclValid(fieldData['ecl']):
        return False
    if not isPidValid(fieldData['pid']):
        return False
    else:
        return True


def CheckPassportData(passports):
    validPassportCount = 0
    for passport in passports:
        isPassportDataValid = hasValidData(passport)
        if isPassportDataValid is True:
            validPassportCount += 1
    print(validPassportCount)


CheckPassportData(validPassports)
