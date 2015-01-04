VOWELS = "aeiouy"

def translate(phrase):
    translation = ''

    while len(phrase) > 0:
        char = phrase[0]
        translation += char

        if char in VOWELS:
            phrase = phrase[3:]
        elif char.isalpha():
            phrase = phrase[2:]
        else:
            phrase = phrase[1:]

    return translation

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
