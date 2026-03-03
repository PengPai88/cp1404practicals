import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALPHABET = VOWELS + CONSONANTS

word_format = input("Enter word format (c=consonant, v=vowel, *=any): ").lower()
word = ''

for kind in word_format:
    if kind == 'c':
        word += random.choice(CONSONANTS)
    elif kind == 'v':
        word += random.choice(VOWELS)
    elif kind == '*':
        word += random.choice(ALPHABET)
    else:
        word += kind

print(word)