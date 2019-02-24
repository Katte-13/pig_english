"""Pig English translation"""
import nltk, re
from nltk.tokenize import RegexpTokenizer

#tokenize the input
intro = '\n--> '

   
def no_consonants(word):
# Return the word with a sufix, if the word has no consonants
    
    consonants = ('b', 'c', 'd', 'f', 'g',
              'h','j', 'k', 'l', 'm','n',
              'p','r', 's', 't', 'v', 'x', 'z', 'w')

    for consonant in consonants:
        if consonant in word:
            return None
    pig_latin = word +'aya'
    return pig_latin

def first_vowel(word):
#Return the word until the first vowel and name it "prefix".Name the rest of the word "stem". Switch them and add sufix.
      
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    for vowel in vowels:
        if vowel in word:
            prefix = word[:(word.index(vowel))]
            stem = word[(word.index(vowel))::]
            pig_latin1 = stem + prefix + 'ay'
            return pig_latin1
    else:
        return None

while True:
    intro = input(intro)
    tokens = nltk.tokenize.RegexpTokenizer("[\\w']+|[^\\w\\s]+").tokenize(intro.lower())
    text = nltk.Text(tokens)
    words_list = []
    for word in text:
        result = no_consonants(word)
        if result:
            words_list.append(result) 
        else: 
            words_list.append(first_vowel(word))
    sentence = ' '.join(words_list)
    print(sentence.capitalize())
