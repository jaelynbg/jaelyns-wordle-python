import tkinter as tk
import pathlib
import random
from string import ascii_letters

from themes_ui import apply_theme, create_theme_selector


NUM_LETTERS = 5
NUM_GUESSES = 6


def add_letter(game, letter):

    if game["game_over"]:
        return

    if len(game["current_guess"]) < NUM_LETTERS:

        game["current_guess"] += letter

        update_current_row(
            game
        )


def create_keyboard(root, game):

    keyboard_frame = tk.Frame(
        root
    )

    keyboard_frame.pack(
        pady=20
    )

    keyboard_buttons = {}
    keyboard_row_frames = []

    rows = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]

    for row_index, row in enumerate(rows):

        row_frame = tk.Frame(
            keyboard_frame
        )

        row_frame.pack()

        keyboard_row_frames.append(
            row_frame
        )

        # -------------------------
        # Enter button
        # -------------------------

        if row_index == 2:

            enter_button = tk.Button(
                row_frame,
                text="ENTER",
                font=("Arial", 12, "bold"),
                width=7,
                height=2,
                relief="flat",
                bd=0,
                highlightthickness=0,
                command=lambda: submit_guess(
                    game
                )
            )

            enter_button.pack(
                side="left",
                padx=2,
                pady=2
            )

            keyboard_buttons["ENTER"] = enter_button

        # -------------------------
        # Letter buttons
        # -------------------------

        for letter in row:

            button = tk.Button(
                row_frame,
                text=letter,
                font=("Arial", 12, "bold"),
                width=4,
                height=2,
                relief="flat",
                bd=0,
                highlightthickness=0,
                command=lambda letter=letter: add_letter(
                    game,
                    letter
                )
            )

            button.pack(
                side="left",
                padx=2,
                pady=2
            )

            keyboard_buttons[letter] = button

        # -------------------------
        # Backspace button
        # -------------------------

        if row_index == 2:

            backspace_button = tk.Button(
                row_frame,
                text="⌫",
                font=("Arial", 12, "bold"),
                width=7,
                height=2,
                relief="flat",
                bd=0,
                highlightthickness=0,
                command=lambda: handle_keypress(
                    type(
                        "Event",
                        (),
                        {
                            "keysym": "BackSpace",
                            "char": ""
                        }
                    )(),
                    game
                )
            )

            backspace_button.pack(
                side="left",
                padx=2,
                pady=2
            )

            keyboard_buttons["BACKSPACE"] = backspace_button

    return (
        keyboard_buttons,
        keyboard_frame,
        keyboard_row_frames
    )


def end_game(game):

    game["game_over"] = True


def new_game(root, game):

    game["word"] = load_game_word()
    game["current_row"] = 0
    game["game_over"] = False

    # Reset keyboard states
    game["keyboard_colors"] = {}

    # Reset board states
    game["board_colors"] = [
        ["empty" for _ in range(NUM_LETTERS)]
        for _ in range(NUM_GUESSES)
    ]

    reset_board(
        game
    )

    reset_keyboard(
        game
    )

    game["current_guess"] = ""

    show_message(
        game["status_label"],
        "Good Luck!",
        None,
        game
    )


def reset_board(game):

    board = game["board"]

    for row in range(NUM_GUESSES):

        for column in range(NUM_LETTERS):

            game["board_colors"][row][column] = "empty"

            box = board[row][column]

            box.config(
                text=""
            )

    # Reapply the currently selected theme
    apply_theme(
        game
    )


def reset_keyboard(game):

    game["keyboard_colors"] = {}

    apply_theme(
        game
    )


def create_window():

    root = tk.Tk()

    root.title(
        "Jaelyn's Wordle"
    )

    root.geometry(
        "1000x1200"
    )

    return root


def load_game_word():

    words_path = pathlib.Path(
        __file__
    ).parent / "solutions.txt"

    word_list = words_path.read_text(
        encoding="utf-8"
    ).split("\n")

    return get_random_word(
        word_list
    )


def create_title(root):

    title = tk.Label(
        root,
        text="JAELYN'S WORDLE",
        font=("Arial", 28, "bold")
    )

    title.pack(
        pady=30
    )

    return title


def create_instructions(root):

    instructions = tk.Label(
        root,
        text="Guess the 5-letter word in 6 attempts!",
        font=("Arial", 14)
    )

    instructions.pack(
        pady=10
    )

    return instructions


def create_status_label(root):

    status_label = tk.Label(
        root,
        text="Good Luck!",
        font=("Arial", 14, "bold")
    )

    status_label.pack(
        pady=5
    )

    return status_label


def create_board(root):

    board = tk.Frame(
        root
    )

    board.pack(
        pady=10
    )

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
                borderwidth=0,
                relief="flat",
                highlightthickness=1,
                takefocus=0
            )

            box.grid(
                row=row,
                column=column,
                padx=3,
                pady=3
            )

            row_boxes.append(
                box
            )

        boxes.append(
            row_boxes
        )

    return board, boxes


def create_game_data(
    word,
    board,
    board_frame,
    status_label,
    keyboard_buttons,
    keyboard_frame,
    keyboard_row_frames
):

    return {

        "word": word,

        "board": board,

        "board_frame": board_frame,

        "status_label": status_label,

        "keyboard_buttons": keyboard_buttons,

        "keyboard_frame": keyboard_frame,

        "keyboard_row_frames": keyboard_row_frames,

        "keyboard_colors": {},

        "board_colors": [
            ["empty" for _ in range(NUM_LETTERS)]
            for _ in range(NUM_GUESSES)
        ],

        "current_row": 0,

        "current_guess": "",

        "game_over": False,

        "theme": "Light",

        "root": None,

        "title": None,

        "instructions": None,

        "new_game_button": None,

        "theme_frame": None,

        "theme_button": None,

        "theme_panel": None,

        "theme_buttons": {},

        "theme_panel_open": False
    }


def show_message(
    status_label,
    message,
    color=None,
    game=None
):

    status_label.config(
        text=message
    )

    if game is not None:

        theme = game["theme"]

        # Let apply_theme control the normal text color
        if color is None:

            from themes import THEMES

            status_label.config(
                fg=THEMES[theme]["app"]["text"]
            )

        else:

            status_label.config(
                fg=color
            )

    elif color is not None:

        status_label.config(
            fg=color
        )


def is_valid_word(guess):

    words_path = pathlib.Path(
        __file__
    ).parent / "guesses.txt"

    word_list = words_path.read_text(
        encoding="utf-8"
    ).split("\n")

    valid_words = {
        word.upper().strip()
        for word in word_list
        if len(word.strip()) == NUM_LETTERS
    }

    return guess in valid_words


def handle_keypress(event, game):

    if game["game_over"]:
        return

    key = event.keysym.upper()

    # -------------------------
    # Backspace
    # -------------------------

    if key == "BACKSPACE":

        if len(game["current_guess"]) > 0:

            game["current_guess"] = (
                game["current_guess"][:-1]
            )

            update_current_row(
                game
            )

        return

    # -------------------------
    # Enter
    # -------------------------

    if key == "RETURN":

        submit_guess(
            game
        )

        return

    # -------------------------
    # Letters A-Z
    # -------------------------

    if len(event.char) == 1 and event.char.isalpha():

        if len(game["current_guess"]) < NUM_LETTERS:

            game["current_guess"] += (
                event.char.upper()
            )

            update_current_row(
                game
            )


def update_current_row(game):

    row = game["current_row"]

    guess = game["current_guess"]

    board = game["board"]

    from themes import THEMES

    theme = THEMES[
        game["theme"]
    ]

    for column in range(NUM_LETTERS):

        box = board[row][column]

        if column < len(guess):

            box.config(
                text=guess[column],
                bg=theme["board"]["empty"],
                fg=theme["app"]["text"],
                borderwidth=0,
                relief="flat",
                highlightthickness=2,
                highlightbackground=theme["board"]["border"],
                highlightcolor=theme["board"]["border"]
            )

        else:

            box.config(
                text="",
                bg=theme["board"]["empty"],
                fg=theme["app"]["text"],
                borderwidth=0,
                relief="flat",
                highlightthickness=2,
                highlightbackground=theme["board"]["border"],
                highlightcolor=theme["board"]["border"]
            )


def submit_guess(game):

    if game["game_over"]:
        return

    guess = game["current_guess"].upper()

    # -------------------------
    # Check length
    # -------------------------

    if len(guess) != NUM_LETTERS:

        show_message(
            game["status_label"],
            "Your guess must be 5 letters!",
            "red"
        )

        return

    # -------------------------
    # Check valid word
    # -------------------------

    if not is_valid_word(guess):

        show_message(
            game["status_label"],
            "❌ Not a valid word!",
            "red"
        )

        return

    # -------------------------
    # Make sure row exists
    # -------------------------

    if game["current_row"] >= NUM_GUESSES:
        return

    word = game["word"]

    current_row = game["current_row"]

    # -------------------------
    # Update board
    # -------------------------

    update_board(
        game,
        current_row,
        guess,
        word
    )

    # -------------------------
    # Update keyboard
    # -------------------------

    update_keyboard(
        game,
        guess,
        word
    )

    # -------------------------
    # Correct guess
    # -------------------------

    if guess == word:

        show_message(
            game["status_label"],
            "🎉 Correct! You got it!",
            "green"
        )

        end_game(
            game
        )

        return

    # -------------------------
    # Move to next row
    # -------------------------

    game["current_row"] += 1

    guesses_left = (
        NUM_GUESSES - game["current_row"]
    )

    if guesses_left == 0:

        show_message(
            game["status_label"],
            f"Game Over! The word was {word}.",
            "red"
        )

        end_game(
            game
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

    game["current_guess"] = ""


def get_letter_colors(
    guess,
    word
):

    colors = [
        "wrong"
    ] * NUM_LETTERS

    remaining_letters = list(
        word
    )

    # -------------------------
    # Correct letters
    # -------------------------

    for column, letter in enumerate(guess):

        if letter == word[column]:

            colors[column] = "correct"

            remaining_letters[column] = None

    # -------------------------
    # Misplaced letters
    # -------------------------

    for column, letter in enumerate(guess):

        if colors[column] == "correct":
            continue

        if letter in remaining_letters:

            colors[column] = "misplaced"

            letter_index = (
                remaining_letters.index(letter)
            )

            remaining_letters[letter_index] = None

    return colors


def update_board(
    game,
    row,
    guess,
    word
):

    colors = get_letter_colors(
        guess,
        word
    )

    board = game["board"]

    for column, letter in enumerate(guess):

        status = colors[column]

        game["board_colors"][row][column] = (
            status
        )

        set_letter_color(
            board[row][column],
            letter,
            status,
            game
        )


def update_keyboard(
    game,
    guess,
    word
):

    colors = get_letter_colors(
        guess,
        word
    )

    color_priority = {
        "wrong": 1,
        "misplaced": 2,
        "correct": 3
    }

    keyboard_colors = (
        game["keyboard_colors"]
    )

    for letter, color in zip(
        guess,
        colors
    ):

        previous_color = (
            keyboard_colors.get(letter)
        )

        if (
            previous_color is None
            or color_priority[color]
            > color_priority[previous_color]
        ):

            keyboard_colors[letter] = color

    # Reapply the theme so the keyboard
    # uses the current theme colors.
    apply_theme(
        game
    )


def set_letter_color(
    box,
    letter,
    color,
    game
):

    from themes import THEMES

    theme = THEMES[
        game["theme"]
    ]

    box.config(
        text=letter,
        bg=theme["board"][color],
        fg="#FFFFFF",
        borderwidth=0,
        relief="flat",
        highlightthickness=0
    )


def get_random_word(word_list):

    words = [

        word.upper()

        for word in word_list

        if len(word) == NUM_LETTERS

        and all(
            letter in ascii_letters
            for letter in word
        )
    ]

    return random.choice(
        words
    )


def main():

    root = create_window()

    word = load_game_word()

    title = create_title(
        root
    )

    instructions = create_instructions(
        root
    )

    status_label = create_status_label(
        root
    )

    board_frame, board = create_board(
        root
    )

    game = create_game_data(
        word,
        board,
        board_frame,
        status_label,
        {},
        None,
        []
    )

    game["root"] = root

    game["title"] = title

    game["instructions"] = instructions

    # -------------------------
    # Create keyboard
    # -------------------------

    (
        keyboard_buttons,
        keyboard_frame,
        keyboard_row_frames
    ) = create_keyboard(
        root,
        game
    )

    game["keyboard_buttons"] = (
        keyboard_buttons
    )

    game["keyboard_frame"] = (
        keyboard_frame
    )

    game["keyboard_row_frames"] = (
        keyboard_row_frames
    )

    # -------------------------
    # Theme selector
    # -------------------------

    create_theme_selector(
        root,
        game
    )

    apply_theme(
        game
    )

    # -------------------------
    # New Game button
    # -------------------------

    new_game_button = tk.Button(
        root,
        text="New Game",
        font=("Arial", 14, "bold"),
        width=12,
        command=lambda: new_game(
            root,
            game
        )
    )

    new_game_button.pack(
        pady=10
    )

    game["new_game_button"] = (
        new_game_button
    )

    # -------------------------
    # Keyboard input
    # -------------------------

    root.bind(
        "<Key>",
        lambda event: handle_keypress(
            event,
            game
        )
    )

    root.focus_force()

    root.mainloop()


if __name__ == "__main__":

    main()