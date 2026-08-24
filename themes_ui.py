import tkinter as tk

from themes import THEMES


def get_current_theme(game):
    return THEMES[game["theme"]]


def change_theme(game, theme_name):
    if theme_name not in THEMES:
        return

    game["theme"] = theme_name

    apply_theme(game)

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

    # -------------------------
    # Main application
    # -------------------------

    root.config(
        bg=theme["app"]["background"]
    )

    title.config(
        bg=theme["app"]["background"],
        fg=theme["app"]["text"]
    )

    instructions.config(
        bg=theme["app"]["background"],
        fg=theme["app"]["text"]
    )

    status_label.config(
        bg=theme["app"]["background"],
        fg=theme["app"]["text"]
    )

    # -------------------------
    # Guess entry
    # -------------------------

    guess_entry.config(
        bg=theme["app"]["background"],
        fg=theme["app"]["text"],
        insertbackground=theme["app"]["text"]
    )

    # -------------------------
    # Board
    # -------------------------

    for row in board:
        for box in row:

            current_color = box.cget("bg")

            # Don't change already colored tiles
            if current_color in (
                theme["board"]["correct"],
                theme["board"]["misplaced"],
                theme["board"]["wrong"]
            ):
                continue

            box.config(
                bg=theme["board"]["empty"],
                fg=theme["app"]["text"],
                highlightbackground=theme["board"]["border"]
            )

    # -------------------------
    # Keyboard
    # -------------------------

    for letter, button in keyboard_buttons.items():

        color = game["keyboard_colors"].get(
            letter,
            "default"
        )

        if color == "green":
            color = theme["keyboard"]["correct"]

        elif color == "gold":
            color = theme["keyboard"]["misplaced"]

        elif color == "gray":
            color = theme["keyboard"]["wrong"]

        else:
            color = theme["keyboard"]["default"]

        button.config(
            bg=color,
            fg=theme["app"]["text"]
        )

    # -------------------------
    # Theme selector
    # -------------------------

    if "theme_frame" in game:
        update_theme_selector(game)


def update_theme_selector(game):

    if "theme_frame" not in game:
        return

    theme = get_current_theme(game)

    theme_frame = game["theme_frame"]
    theme_button = game["theme_button"]
    theme_panel = game["theme_panel"]

    # -------------------------
    # Selector container
    # -------------------------

    theme_frame.config(
        bg=theme["selector"]["background"]
    )

    # -------------------------
    # Main selector button
    # -------------------------

    theme_button.config(
        bg=theme["selector"]["background"],
        fg=theme["selector"]["text"],
        activebackground=theme["selector"]["hover"],
        activeforeground=theme["selector"]["text"],
        text=(
            f"{theme['icon']}  Change Theme    "
            f"{'▲' if game['theme_panel_open'] else '▼'}"
        )
    )

    # -------------------------
    # Dropdown panel
    # -------------------------

    theme_panel.config(
        bg=theme["selector"]["background"],
        highlightbackground=theme["selector"]["border"]
    )

    # -------------------------
    # Theme options
    # -------------------------

    for theme_name, button in game["theme_buttons"].items():

        selected = theme_name == game["theme"]

        if selected:

            button.config(
                bg=theme["selector"]["selected"],
                fg=theme["selector"]["text"],
                activebackground=theme["selector"]["selected"],
                activeforeground=theme["selector"]["text"]
            )

        else:

            button.config(
                bg=theme["selector"]["background"],
                fg=theme["selector"]["text"],
                activebackground=theme["selector"]["hover"],
                activeforeground=theme["selector"]["text"]
            )


def toggle_theme_panel(game):

    theme_panel = game["theme_panel"]

    if game["theme_panel_open"]:

        theme_panel.place_forget()

        game["theme_panel_open"] = False

    else:

        theme_panel.place(
            x=20,
            y=65
        )

        theme_panel.lift()

        game["theme_panel_open"] = True

    update_theme_selector(game)


def create_theme_selector(root, game):

    theme = get_current_theme(game)

    # -------------------------
    # Selector container
    # -------------------------

    theme_frame = tk.Frame(
        root,
        bg=theme["selector"]["background"]
    )

    theme_frame.place(
        x=20,
        y=20
    )

    # -------------------------
    # Main button
    # -------------------------

    theme_button = tk.Button(
        theme_frame,
        text=f"{theme['icon']}  Change Theme    ▼",
        font=("Arial", 11, "bold"),
        bg=theme["selector"]["background"],
        fg=theme["selector"]["text"],
        activebackground=theme["selector"]["hover"],
        activeforeground=theme["selector"]["text"],
        relief="flat",
        bd=0,
        highlightthickness=1,
        highlightbackground=theme["selector"]["border"],
        padx=14,
        pady=10,
        cursor="hand2",
        command=lambda: toggle_theme_panel(game)
    )

    theme_button.pack()

    # -------------------------
    # Dropdown panel
    # -------------------------

    theme_panel = tk.Frame(
        root,
        bg=theme["selector"]["background"],
        bd=1,
        relief="solid"
    )

    theme_buttons = {}

    # -------------------------
    # Theme options
    # -------------------------

    for theme_name, theme_data in THEMES.items():

        button = tk.Button(
            theme_panel,
            text=f"{theme_data['icon']}   {theme_name}",
            font=("Arial", 11, "bold"),
            anchor="w",
            bg=theme["selector"]["background"],
            fg=theme["selector"]["text"],
            activebackground=theme["selector"]["hover"],
            activeforeground=theme["selector"]["text"],
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

    # -------------------------
    # Save UI references
    # -------------------------

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

    game["theme_panel"].place_forget()

    game["theme_panel_open"] = False

    update_theme_selector(game)