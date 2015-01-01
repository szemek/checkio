FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    hundreds, remainder = divmod(number, 100)
    chunks = []

    if hundreds > 0:
        chunks.append(FIRST_TEN[hundreds-1])
        chunks.append('hundred')

    if remainder == 0:
        pass
    elif remainder < 10:
        chunks.append(FIRST_TEN[remainder-1])
    elif remainder < 20:
        chunks.append(SECOND_TEN[remainder%10])
    else:
        tens, remainder = divmod(remainder, 10)
        chunks.append(OTHER_TENS[tens-2])
        if remainder != 0:
            chunks.append(FIRST_TEN[remainder-1])

    result = ' '.join(chunks)

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
