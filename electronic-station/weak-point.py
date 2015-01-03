def weak_point(matrix):
    rows = sums(matrix)
    cols = sums(columns(matrix))

    min_row = rows.index(min(rows))
    min_col = cols.index(min(cols))

    return min_row, min_col

def sums(matrix):
    return map(lambda vector:sum(vector), matrix)

def columns(matrix):
    width = len(matrix[0])
    return [column(matrix, c) for c in range(width)]

def column(matrix, index):
    return map(lambda row:row[index], matrix)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
