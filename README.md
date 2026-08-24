# Jaelyn's Wordle 🎮

A Wordle-inspired word guessing game built with Python and Tkinter.

This project was created as a programming practice project to learn more about Python, GUI development, functions, game logic, file handling, and user input.

## 🎮 About the Game

Jaelyn's Wordle is a desktop word guessing game inspired by the popular game Wordle.

The player has **6 attempts** to guess a randomly selected **5-letter solution word**.

After each valid guess, the game provides feedback:

* 🟩 **Green** — The letter is correct and in the correct position.
* 🟨 **Gold** — The letter is in the word but in the wrong position.
* ⬜ **Gray** — The letter is not in the solution.

The game also handles duplicate letters using Wordle-style letter matching rules.

## ✨ Features

* Randomly selected 5-letter solutions
* 6 guesses per game
* Separate word lists for guesses and solutions
* Valid-word checking
* Duplicate-letter handling
* Green, gold, and gray letter feedback
* On-screen QWERTY keyboard
* Physical keyboard input
* Enter key support
* Keyboard color feedback
* Keyboard color priority
* Incorrect guess messages
* Remaining-guess counter
* Win detection
* Loss detection
* Game-over state
* Input disabled after the game ends
* New Game functionality
* Organized code using separate functions
* External text files for word data

## 🧠 Word Lists

The game uses two separate word lists.

### `guesses.txt`

This file contains words that the player is allowed to guess.

A word can be in this file even if it is not a possible solution.

### `solutions.txt`

This file contains the words that the game can randomly select as the answer.

This allows the game to have a larger list of acceptable guesses while keeping the possible answers separate.

## 📁 Project Files

```text
Jaelyn's Practice Code/
│
├── wordle.py
├── create_wordlist.py
├── guesses.txt
├── solutions.txt
└── README.md
```

### `wordle.py`

Contains the main game and all of the functions used to create and operate the Wordle interface.

### `create_wordlist.py`

A utility script used to process and organize word lists.

### `guesses.txt`

Contains valid words that players can submit as guesses.

### `solutions.txt`

Contains possible words that can be selected as the game's answer.

### `README.md`

Contains documentation about the project.

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** — Used to create the graphical user interface.
* **pathlib** — Used to work with the word-list files.
* **random** — Used to randomly select a solution.
* **string.ascii_letters** — Used when filtering valid words.

## ▶️ How to Run

Make sure Python is installed on your computer.

Open the project folder in VS Code.

Open the terminal and navigate to the project folder.

Run:

```bash
python wordle.py
```

The Wordle game window should open.

## 🎯 How to Play

1. Start the game.
2. Enter a 5-letter word using your physical keyboard or the on-screen keyboard.
3. Press **Enter** to submit your guess.
4. Check the colors of the letters.
5. Use the feedback to improve your next guess.
6. You have a maximum of 6 valid guesses.
7. Guess the solution correctly to win.
8. If all 6 guesses are used, the game ends and the solution is revealed.
9. Click **New Game** to start another game.

## ⌨️ Keyboard Controls

The game supports both physical and on-screen keyboard input.

### Physical Keyboard

Type letters normally using your computer keyboard.

Press:

```text
Enter
```

to submit a guess.

### On-Screen Keyboard

Click the letters displayed on the game's QWERTY keyboard to enter a guess.

## 🟩🟨⬜ Letter Feedback

The game evaluates each letter using Wordle-style rules.

### Green

The letter is in the correct position.

Example:

```text
Answer: TWIST
Guess:  TREAT
        🟩
```

### Gold

The letter exists somewhere in the answer but is in the wrong position.

### Gray

The letter does not have an available match in the answer.

## 🔁 Duplicate Letters

The game includes logic for handling repeated letters.

When a guess contains duplicate letters, the game checks how many copies of that letter actually exist in the solution.

Correct-position matches are evaluated first.

Remaining copies of letters are then used to determine misplaced matches.

This prevents the game from incorrectly marking multiple copies of a letter as present when the solution contains fewer copies.

## 🎮 Game State

The game tracks whether the player is still playing using:

```python
"game_over": False
```

When the player wins or loses, the game state changes to:

```python
"game_over": True
```

Once the game is over, the guess entry is disabled.

## 🔄 New Game

The New Game feature allows the player to restart without closing the application.

Starting a new game:

* Selects a new random solution
* Clears the board
* Resets the guess counter
* Resets keyboard colors
* Clears the current guess
* Re-enables the input field
* Changes the status message back to "Good Luck!"

## 🧩 Project Structure

The project is intentionally organized into many smaller functions.

Examples include:

```python
create_window()
create_title()
create_instructions()
create_status_label()
create_board()
create_keyboard()
create_game_data()
create_guess_entry()
submit_guess()
get_letter_colors()
update_board()
update_keyboard()
set_letter_color()
is_valid_word()
load_game_word()
get_random_word()
new_game()
```

Each function is responsible for a specific part of the application.

This makes the program easier to read, debug, modify, and understand.

## 📚 What This Project Practices

This project is being used to practice several Python programming concepts, including:

* Functions
* Function parameters
* Return values
* Variables
* Constants
* Dictionaries
* Lists
* Sets
* Loops
* Conditional statements
* `if`, `elif`, and `else`
* `for` loops
* `enumerate()`
* Lambda functions
* Dictionaries and dictionary lookups
* String manipulation
* File handling
* List comprehensions
* Set comprehensions
* Random selection
* Object-oriented GUI concepts through Tkinter widgets
* Event handling
* Keyboard events
* GUI state management

## 🚧 Future Improvements

Possible future features include:

* Statistics tracking
* Win percentage
* Current streak
* Best streak
* Guess distribution
* Animated letter reveals
* Improved visual design
* Start screen
* Instructions/help screen
* Dark mode
* Game reset confirmation
* Daily Wordle mode
* Shareable results
* Sound effects
* More polished animations

## 👩🏽‍💻 Author

**Jaelyn Garrard**

This project was created as a hands-on Python programming project to practice building a complete graphical application from the ground up.

---

## 📌 Project Status

**Currently in development.**

New features and improvements will be added as the project continues.
