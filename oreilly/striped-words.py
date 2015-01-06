import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    text = re.sub(r'\W', ' ', text.upper())

    return sum([int(striped(word)) for word in text.split()])

def striped(word):
    index = int(word[0] in CONSONANTS)

    vowels = map(lambda char:char in VOWELS, word[index::2])
    consonants = map(lambda char:char in CONSONANTS, word[1-index::2])

    return all(vowels) and all(consonants) and len(word) >= 2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
