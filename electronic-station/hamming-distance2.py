def checkio(n, m):
    a = binary(n)
    b = binary(m)

    distance = 0

    shorter = min(len(a), len(b))
    zipped = zip(a[:shorter], b[:shorter])
    joined = a[shorter:] + b[shorter:]

    distance += sum(map(lambda (x,y):x^y, zipped))
    distance += sum(joined)

    return distance

def binary(n):
    digits = []

    while n > 0:
        digits.append(n % 2)
        n /= 2

    return digits

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
