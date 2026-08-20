import pathlib
import random
from string import ascii_letters

def main():
    word = get_random_word()
    print("Welcome to Wordle! This is a simple word guessing game. \nYou have 6 attempts to guess the correct 5-letter word. \nGood luck!")

    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()
        show_guess(guess, word)
        if guess == word:
            print("Correct!")
            break
    else:
        game_over(word)


def get_random_word():
    wordlist = pathlib.Path(__file__).parent / "wordlist.txt"
    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").strip().split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guess(guess, word):
    correct_letters = set()
    for letter, correct in zip(guess, word):
        if letter == correct:
            correct_letters.add(letter)

    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

def game_over(word):
    print(f"\nSorry, you've used all your guesses. The correct word was: {word}")

if __name__ == "__main__":
    main()