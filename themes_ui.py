import tkinter as tk

from themes import THEMES


def get_current_theme(game):
    return THEMES[game["theme"]]


def change_theme(game, theme_name):
    if theme_name not in THEMES:
        return

    game["theme"] = theme_name

    apply_theme(game)

    # Update the theme selector
    update_theme_selector(game)


def apply_theme(game):
    theme = get_current_theme(game)

    root = game["root"]
    title = game["title"]
    instructions = game["instructions"]
    status_label = game["status_label"]
    guess_entry = game["guess_entry"]
    keyboard_buttons = game["keyboard_buttons"]
    board = game["board"]

    # Main window
    root.config(
        bg=theme["background"]
    )

    # Text
    title.config(
        bg=theme["background"],
        fg=theme["text"]
    )

    instructions.config(
        bg=theme["background"],
        fg=theme["text"]
    )

    status_label.config(
        bg=theme["background"]
    )

    # Guess entry
    guess_entry.config(
        bg=theme["background"],
        fg=theme["text"],
        insertbackground=theme["text"]
    )

    # Board
    for row in board:
        for box in row:

            # Don't destroy an already-colored guess tile
            current_color = box.cget("bg")

            if current_color in ("green", "gold", "gray"):
                continue

            box.config(
                bg=theme["background"],
                fg=theme["text"],
                highlightbackground=theme["border"]
            )

    # Keyboard
    for letter, button in keyboard_buttons.items():

        color = game["keyboard_colors"].get(
            letter,
            theme["keyboard"]
        )

        # Convert game colors into the current theme colors
        if color == "green":
            color = theme["correct"]

        elif color == "gold":
            color = theme["misplaced"]

        elif color == "gray":
            color = theme["wrong"]

        button.config(
            bg=color,
            fg=theme["text"]
        )

    # Theme selector
    if "theme_frame" in game:
        update_theme_selector(game)


def update_theme_selector(game):
    if "theme_frame" not in game:
        return

    theme = get_current_theme(game)

    theme_frame = game["theme_frame"]
    theme_button = game["theme_button"]
    theme_panel = game["theme_panel"]

    # Update selector colors
    theme_frame.config(
        bg=theme["background"]
    )

    theme_button.config(
        bg=theme["keyboard"],
        fg=theme["text"],
        activebackground=theme["border"],
        activeforeground=theme["text"],
        text=f"{theme['icon']}  Change Theme    {'▲' if game['theme_panel_open'] else '▼'}"
    )

    theme_panel.config(
        bg=theme["background"]
    )

    # Update every theme button
    for theme_name, button in game["theme_buttons"].items():

        selected = theme_name == game["theme"]

        if selected:
            button.config(
                bg=theme["border"],
                fg=theme["text"],
                activebackground=theme["border"],
                activeforeground=theme["text"]
            )

        else:
            button.config(
                bg=theme["background"],
                fg=theme["text"],
                activebackground=theme["border"],
                activeforeground=theme["text"]
            )


def toggle_theme_panel(game):
    theme_panel = game["theme_panel"]

    if game["theme_panel_open"]:
        theme_panel.place_forget()
        game["theme_panel_open"] = False

    else:
        theme_panel.place(
            x=0,
            y=48
        )

        game["theme_panel_open"] = True

    update_theme_selector(game)


def create_theme_selector(root, game):
    theme = get_current_theme(game)

    # Main selector container
    theme_frame = tk.Frame(
        root,
        bg=theme["background"]
    )

    theme_frame.place(
        x=20,
        y=20
    )

    # Main "Change Theme" button
    theme_button = tk.Button(
        theme_frame,
        text=f"{theme['icon']}  Change Theme    ▼",
        font=("Arial", 11, "bold"),
        bg=theme["keyboard"],
        fg=theme["text"],
        activebackground=theme["border"],
        activeforeground=theme["text"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        padx=14,
        pady=10,
        cursor="hand2",
        command=lambda: toggle_theme_panel(game)
    )

    theme_button.pack()

    # Dropdown panel
    theme_panel = tk.Frame(
        theme_frame,
        bg=theme["background"],
        bd=1,
        relief="solid"
    )

    theme_buttons = {}

    for theme_name, theme_data in THEMES.items():

        button = tk.Button(
            theme_panel,
            text=f"{theme_data['icon']}   {theme_name}",
            font=("Arial", 11, "bold"),
            anchor="w",
            bg=theme["background"],
            fg=theme["text"],
            activebackground=theme["border"],
            activeforeground=theme["text"],
            relief="flat",
            bd=0,
            highlightthickness=0,
            width=22,
            padx=12,
            pady=9,
            cursor="hand2",
            command=lambda name=theme_name: select_theme(
                game,
                name
            )
        )

        button.pack(
            fill="x",
            padx=5,
            pady=2
        )

        theme_buttons[theme_name] = button

    # Save UI references in game
    game["theme_frame"] = theme_frame
    game["theme_button"] = theme_button
    game["theme_panel"] = theme_panel
    game["theme_buttons"] = theme_buttons
    game["theme_panel_open"] = False

    return theme_frame


def select_theme(game, theme_name):
    change_theme(
        game,
        theme_name
    )

    # Close panel after selection
    game["theme_panel"].place_forget()
    game["theme_panel_open"] = False

    update_theme_selector(game)