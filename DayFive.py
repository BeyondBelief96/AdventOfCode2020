# PART ONE

with open("boardingpasses.txt") as file:
    boardingPasses = file.readlines()
    boardingPasses = [line.strip() for line in boardingPasses]

takenSeats = []


def LowerSplit(list):
    return list[:len(list)//2]


def UpperSplit(list):
    return list[len(list)//2:]


def FindSeat(boardingPass):
    rows = range(0, 128)
    cols = range(0, 8)

    row = 0
    col = 0

    for val in boardingPass:
        if val == 'F' or 'B':
            if val == 'F':
                rows = LowerSplit(rows)
            if val == 'B':
                rows = UpperSplit(rows)
        if val == 'L' or 'R':
            if val == 'L':
                cols = LowerSplit(cols)
            if val == 'R':
                cols = UpperSplit(cols)

    row = rows[0]
    col = cols[0]
    takenSeats.append((row, col))

    id = 8 * row + col
    return id


def CheckBoardingPasses(boardingPasses):
    seatIds = []
    for boardingPass in boardingPasses:
        id = FindSeat(boardingPass)
        seatIds.append(id)

    print(f"The maximum seat id is : {max(seatIds)}")


CheckBoardingPasses(boardingPasses)

# PART TWO

takenSeats.sort()
orderedSeatIds = []

for pair in takenSeats:
    id = pair[0] * 8 + pair[1]
    orderedSeatIds.append(id)


def FindMissingSeatId(idList):
    missingId = 0
    mockList = list(range(49, 807))
    for id in mockList:
        if id not in idList:
            missingId = id
    print(f"My seat id is: {missingId}")


FindMissingSeatId(orderedSeatIds)
