import sys
nato_alfabet = {
    'a': 'alfa',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu',
    'æ': 'Ærlig',
    'ø': 'Østen',
    'å': 'Åse'
}

nato_tall = {
    '0': 'null',
    '1': 'en',
    '2': 'to',
    '3': 'tre',
    '4': 'fire',
    '5': 'fem',
    '6': 'seks',
    '7': 'syv',
    '8': 'åtte',
    '9': 'ni'
}

try:
    word = sys.argv[1]
except IndexError:
    print('Usage: alfabet.py <word>')
    exit(1)

for letter in word:
    if letter.lower() in nato_alfabet:
        print(nato_alfabet[letter.lower()])
    else:
        print(letter)

for number in word:
    if number in nato_tall:
        print(nato_tall[number])
    else:
        print(number)        