from math import radians
import random
import string
from words import words

def  get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

def hangman():
    word =get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_leeters = set()

