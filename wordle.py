import tkinter as tk
import pathlib
import random
from string import ascii_letters


NUM_LETTERS = 5
NUM_GUESSES = 6

def create_keyboard(root, guess_entry, submit_guess):
    keyboard_frame = tk.Frame(root)
    keyboard_frame.pack(pady=20)

    rows = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]

    for row_index, row in enumerate(rows):
        row_frame = tk.Frame(keyboard_frame)
        row_frame.pack()

        for letter in row:
            button = tk.Button(
                row_frame,
                text=letter,
                font=("Arial", 12, "bold"),
                width=4,
                height=2,
                command=lambda letter=letter: add_letter(
                    guess_entry, letter
                )
            )
            button.pack(side="left", padx=2, pady=2)

    backspace_button = tk.Button(
        keyboard_frame,
        text="⌫",
        font=("Arial", 12, "bold"),
        width=6,
        height=2,
        command=lambda: remove_letter(guess_entry)
    )
    backspace_button.pack(pady=5)

    enter_button = tk.Button(
        keyboard_frame,
        text="ENTER",
        font=("Arial", 12, "bold"),
        width=10,
        height=2,
        command=submit_guess
    )
    enter_button.pack(pady=5)

def add_letter(guess_entry, letter):
    current_guess = guess_entry.get()

    if len(current_guess) < 5:
        guess_entry.insert(tk.END, letter)


def remove_letter(guess_entry):
    current_guess = guess_entry.get()

    if current_guess:
        guess_entry.delete(len(current_guess) - 1, tk.END)

def main():
    root = create_window()

    word = load_game_word()

    title = create_title(root)
    instructions = create_instructions(root)
    status_label = create_status_label(root)
    board = create_board(root)

    game = create_game_data(word, board, status_label)

    guess_entry = create_guess_entry(root)

    create_keyboard(
        root,
        guess_entry,
        lambda: submit_guess(guess_entry, game)
    )

    root.mainloop()

    
def create_window():
    root = tk.Tk()
    root.title("Jaelyn's Wordle")
    root.geometry("1000x1000")

    return root


def load_game_word():
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"

    word_list = words_path.read_text(
        encoding="utf-8"
    ).split("\n")

    return get_random_word(word_list)


def create_title(root):
    title = tk.Label(
        root,
        text="JAELYN'S WORDLE",
        font=("Arial", 28, "bold")
    )
    title.pack(pady=30)

    return title


def create_instructions(root):
    instructions = tk.Label(
        root,
        text="Guess the 5-letter word in 6 attempts!",
        font=("Arial", 14)
    )
    instructions.pack(pady=10)

    return instructions

def create_status_label(root):
    status_label = tk.Label(
        root,
        text="Good Luck!",
        font=("Arial", 14, "bold")
    )
    status_label.pack(pady=5)

    return status_label

def create_board(root):
    board = tk.Frame(root)
    board.pack(pady=20)

    boxes = []

    for row in range(NUM_GUESSES):
        row_boxes = []

        for column in range(NUM_LETTERS):
            box = tk.Label(
                board,
                text="",
                font=("Arial", 24, "bold"),
                width=4,
                height=2,
                borderwidth=2,
                relief="solid"
            )

            box.grid(
                row=row,
                column=column,
                padx=5,
                pady=5
            )

            row_boxes.append(box)

        boxes.append(row_boxes)

    return boxes


def create_game_data(word, board, status_label):
    return {
        "word": word,
        "board": board,
        "status_label": status_label,
        "current_row": 0
    }

def show_message(status_label, message, color):
    status_label.config(
        text=message,
        fg=color
    )

def create_guess_entry(root):
    guess_entry = tk.Entry(
        root,
        font=("Arial", 20),
        justify="center"
    )

    guess_entry.pack(pady=15)

    return guess_entry


def create_guess_button(root, guess_entry, game):
    guess_button = tk.Button(
        root,
        text="GUESS",
        font=("Arial", 14, "bold"),
        width=10,
        command=lambda: submit_guess(
            guess_entry,
            game
        )
    )

    guess_button.pack()

    return guess_button


def submit_guess(guess_entry, game):
    guess = guess_entry.get().upper()

    if len(guess) != NUM_LETTERS:
        show_message(
            game["status_label"],
            "Your guess must be 5 letters!",
            "red"
        )
        return

    word = game["word"]
    board = game["board"]
    current_row = game["current_row"]

    update_board(
        board,
        current_row,
        guess,
        word
    )

    if guess == word:
        show_message(
            game["status_label"],
            "🎉 Correct! You got it!",
            "green"
        )
        return

    game["current_row"] += 1

    guesses_left = NUM_GUESSES - game["current_row"]

    if guesses_left == 0:
        show_message(
            game["status_label"],
            f"Game Over! The word was {word}.",
            "red"
        )

    elif guesses_left == 1:
        show_message(
            game["status_label"],
            "Incorrect! You have 1 guess left!",
            "red"
        )

    else:
        show_message(
            game["status_label"],
            f"Incorrect! You have {guesses_left} guesses remaining.",
            "red"
        )

    guess_entry.delete(0, tk.END)
def update_board(board, row, guess, word):
    for column, letter in enumerate(guess):

        if letter == word[column]:
            set_letter_color(
                board[row][column],
                letter,
                "green"
            )

        elif letter in word:
            set_letter_color(
                board[row][column],
                letter,
                "gold"
            )

        else:
            set_letter_color(
                board[row][column],
                letter,
                "gray"
            )


def set_letter_color(box, letter, color):
    box.config(
        text=letter,
        bg=color,
        fg="white"
    )


def get_random_word(word_list):
    words = [
        word.upper()
        for word in word_list
        if len(word) == NUM_LETTERS
        and all(letter in ascii_letters for letter in word)
    ]

    return random.choice(words)


if __name__ == "__main__":
    main()