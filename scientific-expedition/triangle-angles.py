from math import asin, degrees, sqrt

def checkio(a, b, c):
    result = [0, 0, 0]

    if (a + b > c) and (a + c > b) and (b + c > a):
        P = area(a, b, c)
        R = radius(a, b, c, P)
        D = 2.0 * R

        alpha = angle(a, b, c, D)
        beta = angle(b, a, c, D)
        gamma = angle(c, a, b, D)

        result = sorted([alpha, beta, gamma])

    return result

# http://en.wikipedia.org/wiki/Law_of_sines
# http://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Principal_values

def angle(a, b, c, D):
    result = degrees(asin(a / D))
    if b ** 2 + c ** 2 < a ** 2:
        return round(180 - result)
    else:
        return round(result)

def area(a, b, c):
    p = (a + b + c) / 2.0
    return sqrt(p * (p - a) * (p - b) * (p - c))

def radius(a, b, c, P):
    return (a * b * c) / (4.0 * P)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(5,4,3) == [37,53,90]
    assert checkio(11,20,30) == [11,20,149]
