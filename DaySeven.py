with open("rules.txt") as file:
    rules = file.readlines()
    rules = [line.strip() for line in rules]


def get_num_bags(color):
    allColors = []
    linesContaingColor = [
        line for line in rules if color in line and line.index(color) != 0]

    if len(linesContaingColor) == 0:
        return []
    else:
        colors = [line[:line.index(
            ' bags')] for line in linesContaingColor]
        colors = [color for color in colors if color not in allColors]

        for color in colors:
            allColors.append(color)
            bags = get_num_bags(color)

            allColors += bags

        uniqueColors = []
        for color in allColors:
            if color not in uniqueColors:
                uniqueColors.append(color)
        return uniqueColors


colors = get_num_bags('shiny gold')
print(len(colors))


# PART TWO

def get_bag_count(color):
    lineContainingColor = [
        line for line in rules if color in line and line.index(color) == 0]

    rule = lineContainingColor[0]

    if 'no' in rule:
        return 1

    rule = rule[rule.index('contain') + 8:].split()

    i = 0
    total = 0
    while i < len(rule):
        count = int(rule[i])
        color = rule[i + 1] + ' ' + rule[i + 2]
        total += count * get_bag_count(color)

        i += 4
    if color == 'shiny gold':
        return total
    else:
        return total + 1


totalBagCount = get_bag_count('shiny gold')
print(totalBagCount)
# REDUCE TOTAL BY ONE. DONT KNOW WHY YET
