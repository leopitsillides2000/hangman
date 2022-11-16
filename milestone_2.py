import random

word_list = ["orange", "apple", "melon", "blueberry", "grape"]

print(word_list)

word = random.choice(word_list)

print(word)


while True:
    guess = input("Please enter a single letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
        break
    else:
        print("Oops! That is not a valid input.")

