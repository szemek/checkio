def checkio(data):
    if len(data) > 0:
        return data[0] + checkio(data[1:])
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([1, 2, 3]) == 6
    assert checkio([2, 2, 2, 2, 2, 2]) == 12
