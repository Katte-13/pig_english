"""Pig English translation"""
import re

intro = '\n--> '

while True:
    word = input(intro)
    """word = re.findall(r'\w+', text)"""
    
    def no_consonants(word): """ Return the word with a sufix,
if the word has no consonants""" 
    
    consonants = ('b', 'c', 'd', 'f', 'g',
              'h','j', 'k', 'l', 'm','n',
              'p','r', 's', 't', 'v', 'x', 'z', 'w')

    for consonant in consonants:
        if consonant not in list(word):
            pig_latin = word +'aya'
            print(pig_latin)
            break
        

    def first_vowel(word): """Return the word until the first vowel and name it "prefix".
    Name the rest of the word "stem". Switch them and add 'ay'."""
      
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    for vowel in vowels:
        if vowel in word:
            prefix = word[:(word.index(vowel))]
            stem = word[(word.index(vowel))::]
            pig_latin1 = stem + prefix + 'ay'
            print(pig_latin1)
            break

