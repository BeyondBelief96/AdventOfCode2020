with open('trees.txt') as file:
    map = file.readlines()
    map = [line.strip() for line in map]
    del map[323]

tree = '#'
treeCount1 = 0
treeCount2 = 0
treeCount3 = 0
treeCount4 = 0
treeCount5 = 0


def count_trees(columnCounter, rowCounter):
    row, col = 0, 0
    _treeCount = 0
    while row+1 < len(map):
        row += rowCounter
        col += columnCounter

        space = map[row][col % len(map[row])]

        if(space == tree):
            _treeCount += 1
    return _treeCount


treeCount1 = count_trees(1, 1)
treeCount2 = count_trees(3, 1)
treeCount3 = count_trees(5, 1)
treeCount4 = count_trees(7, 1)
treeCount5 = count_trees(1, 2)

answer = treeCount1 * treeCount2 * treeCount3 * treeCount4 * treeCount5
print(answer)
