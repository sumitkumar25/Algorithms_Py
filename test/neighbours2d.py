matrix = [
    [11, 21, 31, 41, 51, 61, 71],
    [12, 22, 32, 42, 52, 62, 72],
    [13, 23, 33, 43, 53, 63, 73],
    [14, 24, 34, 44, 54, 64, 74],
    [15, 25, 35, 45, 55, 65, 75],
    [16, 26, 36, 46, 56, 66, 76],
    [17, 27, 37, 47, 57, 67, 77]]


def in_bounds(matrix, row, col):
    if row < 0 or col < 0:
        return False
    if row > len(matrix)-1 or col > len(matrix)-1:
        return False
    return True


def neighbors(matrix, radius, rowNumber, colNumber):
    for row in range(radius):
        for col in range(radius):
            if in_bounds(matrix, rowNumber+row, colNumber+col):
                print('neighbors at', rowNumber+row, colNumber+col, 'is',  matrix[rowNumber+row][colNumber+col])


neighbors(matrix, 4, 1, 1)
