#Lindsey Caldwell
#3/27/17
#Word Jumble

#the computer picks a random word and then "jumbles" it
#the player has to guess the original word

import random

#create a sentence of words to choose from

WORDS = ("oyster", "river", "high", "school", "is", "cool")

#pick one word randomly from the sequence

word = random.choice(WORDS)

#create a variable to use later to see if the guess is correct
correct = word

#create a jumbled version of the word
jumble=""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#start the game
print(
    """
               Welcome to Word Jumble!

         Unscramble the letters to make a word.
       (Press the enter key at the promt to quit.)
    """
    )
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess !="":
    print("Sorry, that's not it.")
    guess = input ("Your guess: ")

if guess == correct:
    print("That's it! You've guessed it!\n")

print("Thanks for palying.")

input("\n\nPress the enter key to exit.")










    
