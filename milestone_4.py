import random

class Hangman:
    def __init__(self, word_list):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for x in self.word]
        self.num_letters = len(self.word)
        self.num_lives = 5
        self.word_list = word_list
        self.list_of_guesses = []

#print(Hangman(['apple', 'pear']).word_guessed)

