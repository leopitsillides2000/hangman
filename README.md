# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1

- General set up of the development environment including the git repository 'hangman' and its correspondence with GitHub.

## Milestone 2

- Setup of the 'word_list' variable giving a selection of 5 fruits.


```
word_list = ["orange", "apple", "melon", "blueberry", "grape"]
```

- The 'random' module randomly selects a word from the specified list of fruit and assigns the selected fruit to a variable 'word'.
- The user is given the option to input a guess letter which has conditional statements such the the input is both a single character and is in the alphabet.

## Milestone 3

- Encases conditional statements in a while loop to ensure input is repeated until valid.
- Creates another conditional statement to notify the user of whether the guess is in the word.
- Wraps the latter condtional statement in a function called 'check_guess' and then writes in a function 'ask_for_input' that utilises the former conditional statement and the check_guess function.

## Milestone 4

- Creates a class 'Hangman' that will contain the code for the game.
- Within the 'Hangman' class key attributes 
```
word
```
```
word_guessed
```
```
num_letters
```
```
num_lives
```
```
word_list
```
```
list_of_guesses
```
are initialised so that they can be kept track of during the proceedings of the game.
- Two methods were introduced, these were simply variations of the functions from milestone 3, 'check_guess' and 'ask_for_input'.
