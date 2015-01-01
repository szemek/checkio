def checkio(game_result):
    for line in lines(game_result):
        if line == u'XXX':
            return 'X'
        elif line == u'OOO':
            return 'O'

    return 'D'

def lines(array):
    return rows(array) + columns(array) + diagonals(array)

def rows(array):
    return array

def columns(array):
    return [column(array, c) for c in range(3)]

def column(array, index):
    return ''.join(map(lambda row:row[index], array))

def diagonals(array):
    return [
        ''.join([array[i][i] for i in range(3)]),
        ''.join([array[i][2-i] for i in range(3)])
    ]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

