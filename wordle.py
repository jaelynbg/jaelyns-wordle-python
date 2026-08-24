import tkinter as tk
import pathlib
import random
from string import ascii_letters

from themes_ui import apply_theme, create_theme_selector


NUM_LETTERS = 5
NUM_GUESSES = 6

def create_keyboard(root, guess_entry):
    keyboard_frame = tk.Frame(root)
    keyboard_frame.pack(pady=20)

    keyboard_buttons = {}

    rows = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]

    for row in rows:
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

            keyboard_buttons[letter] = button

    return keyboard_buttons


def add_letter(guess_entry, letter):
    current_guess = guess_entry.get()

    if len(current_guess) < NUM_LETTERS:
        guess_entry.insert(tk.END, letter)

def disable_guess_entry(guess_entry):
    guess_entry.config(state="disabled")

def end_game(game, guess_entry):
    game["game_over"] = True
    disable_guess_entry(guess_entry)

def new_game(root, game, guess_entry):
    # Reset the game state
    game["word"] = load_game_word()
    game["current_row"] = 0
    game["game_over"] = False
    game["keyboard_colors"] = {}

    reset_board(game["board"])
    reset_keyboard(game["keyboard_buttons"])
    reset_guess_entry(guess_entry)

    show_message(
        game["status_label"],
        "Good Luck!",
        "black"
    )

def reset_board(board):
    for row in board:
        for box in row:
            box.config(
                text="",
                bg="SystemButtonFace",
                fg="black"
            )

def reset_keyboard(keyboard_buttons):
    for button in keyboard_buttons.values():
        button.config(
            bg="SystemButtonFace",
            fg="black"
        )

def reset_guess_entry(guess_entry):
    guess_entry.config(state="normal")
    guess_entry.delete(0, tk.END)
    guess_entry.focus()

def create_window():
    root = tk.Tk()
    root.title("Jaelyn's Wordle")
    root.geometry("1000x1200")

    return root


def load_game_word():
    words_path = pathlib.Path(__file__).parent / "solutions.txt"

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
    board.pack(pady=10)

    boxes = []

    for row in range(NUM_GUESSES):
        row_boxes = []

        for column in range(NUM_LETTERS):
            box = tk.Label(
                board,
                text="",
                font=("Arial", 18, "bold"),
                width=5,
                height=2,
                borderwidth=2,
                relief="solid"
            )

            box.grid(
                row=row,
                column=column,
                padx=3,
                pady=3
            )

            row_boxes.append(box)

        boxes.append(row_boxes)

    return boxes


def create_game_data(word, board, status_label, keyboard_buttons):
    return {
        "word": word,
        "board": board,
        "status_label": status_label,
        "keyboard_buttons": keyboard_buttons,
        "keyboard_colors": {},
        "current_row": 0,
        "game_over": False,
        "theme": "Light",
        "root": None,
        "title": None,
        "instructions": None,
        "guess_entry": None,
        "new_game_button": None,
        "theme_frame": None,
        "theme_button": None,
        "theme_panel": None,
        "theme_buttons": {},
        "theme_panel_open": False
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


def is_valid_word(guess):
    words_path = pathlib.Path(__file__).parent / "guesses.txt"

    word_list = words_path.read_text(
        encoding="utf-8"
    ).split("\n")

    valid_words = {
        word.upper().strip()
        for word in word_list
        if len(word.strip()) == NUM_LETTERS
    }

    return guess in valid_words



def submit_guess(guess_entry, game):
    if game["game_over"]:
        return
    
    guess = guess_entry.get().upper()

    if len(guess) != NUM_LETTERS:
        show_message(
            game["status_label"],
            "Your guess must be 5 letters!",
            "red"
        )
        return

    if not is_valid_word(guess):
        show_message(
            game["status_label"],
            "❌ Not a valid word!",
            "red"
        )
        return

    if game["current_row"] >= NUM_GUESSES:
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

    update_keyboard(
        game["keyboard_buttons"],
        game["keyboard_colors"],
        guess,
        word
    )

    if guess == word:
        show_message(
            game["status_label"],
            "🎉 Correct! You got it!",
            "green"
        )

        end_game(game, guess_entry)
        return

    game["current_row"] += 1

    guesses_left = NUM_GUESSES - game["current_row"]

    if guesses_left == 0:
        show_message(
            game["status_label"],
            f"Game Over! The word was {word}.",
            "red"
        )

        end_game(game, guess_entry)
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

def get_letter_colors(guess, word):
    colors = ["gray"] * NUM_LETTERS

    # Make a copy of the answer.
    # We use this to keep track of which letters
    # are still available to match.
    remaining_letters = list(word)

    # STEP 1:
    # Find letters that are in the correct position.
    for column, letter in enumerate(guess):

        if letter == word[column]:
            colors[column] = "green"

            # This copy of the letter has now been used.
            remaining_letters[column] = None

    # STEP 2:
    # Find letters that exist in the word
    # but are in the wrong position.
    for column, letter in enumerate(guess):

        if colors[column] == "green":
            continue

        if letter in remaining_letters:
            colors[column] = "gold"

            # Use up this copy of the letter.
            letter_index = remaining_letters.index(letter)
            remaining_letters[letter_index] = None

    return colors


def update_board(board, row, guess, word):
    colors = get_letter_colors(
        guess,
        word
    )

    for column, letter in enumerate(guess):
        set_letter_color(
            board[row][column],
            letter,
            colors[column]
        )


def update_keyboard(keyboard_buttons, keyboard_colors, guess, word):
    colors = get_letter_colors(
        guess,
        word
    )

    # Green is the highest priority.
    color_priority = {
        "gray": 1,
        "gold": 2,
        "green": 3
    }

    for letter, color in zip(guess, colors):

        previous_color = keyboard_colors.get(letter)

        # Only update the keyboard if this result
        # is better than the previous result.
        if (
            previous_color is None
            or color_priority[color] > color_priority[previous_color]
        ):
            keyboard_colors[letter] = color

            keyboard_buttons[letter].config(
                bg=color,
                fg="white"
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

def main():
    root = create_window()

    word = load_game_word()

    title = create_title(root)
    instructions = create_instructions(root)
    status_label = create_status_label(root)
    board = create_board(root)

    guess_entry = create_guess_entry(root)

    keyboard_buttons = create_keyboard(
        root,
        guess_entry
    )

    game = create_game_data(
        word,
        board,
        status_label,
        keyboard_buttons
    )

    game["root"] = root
    game["title"] = title
    game["instructions"] = instructions
    game["guess_entry"] = guess_entry

    create_theme_selector(root, game)
    apply_theme(game)


    new_game_button = tk.Button(
        root,
        text = "New Game",
        font = ("Arial", 14, "bold"),
        width = 12,
        command = lambda: new_game(root, game, guess_entry)
    )
    new_game_button.pack(pady=10)

    guess_entry.bind(
        "<Return>",
        lambda event: submit_guess(guess_entry, game)
    )

    root.mainloop()



if __name__ == "__main__":
    main()