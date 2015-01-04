import re

def find_word(message):
    words = map(lambda word:re.sub(r'\W', '', word), message.lower().split())

    coefficients = [[] for i in range(len(words))]

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            value = coefficient(words[i], words[j])

            coefficients[i].append(value)
            coefficients[j].append(value)

    averages = map(lambda array:float(sum(array))/len(array), coefficients)

    result = words[len(averages) - averages[::-1].index(max(averages)) - 1]

    return result

def coefficient(a, b):
    result = 0.0

    result += rule1(a, b)
    result += rule2(a, b)
    result += rule3(a, b)
    result += rule4(a, b)

    return result

def rule1(a, b):
    return 10.0 if a[0] == b[0] else 0.0

def rule2(a, b):
    return 10.0 if a[-1] == b[-1] else 0.0

def rule3(a, b):
    if len(a) <= len(b):
        return 30.0 * len(a) / len(b)
    else:
        return 30.0 * len(b) / len(a)

def rule4(a, b):
    a = set(a)
    b = set(b)
    c = a.intersection(b)
    u = a.union(b)

    common = len(c)
    unique = len(u)

    return 50.0 * common / unique

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
