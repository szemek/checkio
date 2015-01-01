def checkio(expression):
    stack = []

    for char in expression:
        if char in ['{', '(', '[']:
            stack.append(char)
        elif char in ['}', ')', ']']:
            if len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if not matching(last, char):
                    return False

    return len(stack) == 0

def matching(opening, closing):
    brackets = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    return brackets[opening] == closing

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio(u"2+3") == True, "No brackets, no problem"
