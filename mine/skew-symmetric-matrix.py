def checkio(matrix):
    return matrix == negative(transpose(matrix))

def negative(matrix):
    return map(lambda row:map(lambda x:-x, row), matrix)

def transpose(matrix):
    return columns(matrix)

def columns(matrix):
    width = len(matrix[0])
    return [column(matrix, c) for c in range(width)]

def column(matrix, index):
    return map(lambda row:row[index], matrix)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
