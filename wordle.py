import pathlib
import random
from string import ascii_letters


WORDLIST = pathlib.Path("wordlist.txt")

words = [
    word.upper()
    for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
]
word = random.choice(words)

#creating for loop to ask user to guess the word 6 times
#creating variable for user inputs
    #guess num - which guess the user is on
    #printing the guess number and asking user to input their guess
    #using a f string to format the output
    #using .upper() to convert the input to uppercase

print("Welcome to Wordle! You have 6 guesses to find the correct word.")
for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == word:
        print("Correct!")
        break
    
    #print("Try Again.")

    # correct_letters = {
    #     letter for letter, correct in zip(guess, word) if letter == correct
    # }
    # misplaced_letters = set(guess) & set(word) - correct_letters
    # wrong_letters = set(guess) - set(word)

    correct_letters = set()

    #for each char in guess, find the correct letters from comparaing
    #guess and word including position, and if those characters 
    # ('letters') are the same, 
    # add them to the correct_letters set

    for letter, correct in zip(guess, word):
        if letter == correct:
            correct_letters.add(letter)

    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))
else:
    print(f"\nSorry, you've used all your guesses. The correct word was: {word}")