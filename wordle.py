import tkinter as tk
import pathlib
import random
from string import ascii_letters


def main():
    root = tk.Tk()
    root.title("Jaelyn's Wordle")
    root.geometry("800x600")

    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(
        words_path.read_text(encoding="utf-8").split("\n")
    )

    title = tk.Label(
        root,
        text="JAELYN'S WORDLE",
        font=("Arial", 28, "bold")
    )
    title.pack(pady=30)

    instructions = tk.Label(
        root,
        text="Guess the 5-letter word in 6 attempts!",
        font=("Arial", 14)
    )
    instructions.pack(pady=10)

    board = tk.Frame(root)
    board.pack(pady=20)

    boxes = []

    for row in range(6):
        row_boxes = []

        for column in range(5):
            box = tk.Label(
                board,
                text="",
                font=("Arial", 24, "bold"),
                width=4,
                height=2,
                borderwidth=2,
                relief="solid"
            )
            box.grid(row=row, column=column, padx=5, pady=5)
            row_boxes.append(box)

        boxes.append(row_boxes)

    guess_entry = tk.Entry(
        root,
        font=("Arial", 20),
        justify="center"
    )
    guess_entry.pack(pady=15)

    guess_button = tk.Button(
        root,
        text="GUESS",
        font=("Arial", 14, "bold"),
        width=10
    )
    guess_button.pack()

    root.mainloop()


def get_random_word(word_list):
    words = [
        word.upper()
        for word in word_list
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