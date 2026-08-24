# Jaelyn's Wordle 🎮

A Wordle-inspired word guessing game built with Python and Tkinter.

This project was created as a programming practice project to learn more about Python, GUI development, functions, game logic, file handling, user input, and Git version control.

---

# 🎮 About the Game

Jaelyn's Wordle is a desktop word guessing game inspired by the popular game Wordle.

The player has 6 attempts to guess a randomly selected 5-letter solution word.

After each valid guess, the game provides feedback:

🟩 **Green** — The letter is correct and in the correct position.

🟨 **Gold** — The letter is in the word but in the wrong position.

⬜ **Gray** — The letter is not in the solution.

The game also handles duplicate letters using Wordle-style letter matching rules.

<<<<<<< HEAD
✨ Features
Randomly selected 5-letter solutions
6 guesses per game
Separate word lists for guesses and solutions
Valid-word checking
Duplicate-letter handling
Green, gold, and gray letter feedback
On-screen QWERTY keyboard
Physical keyboard input
Enter key support
Keyboard color feedback
Keyboard color priority
Incorrect guess messages
Remaining-guess counter
Win detection
Loss detection
Game-over state
Input disabled after the game ends
New Game functionality
Multiple visual themes
Light mode
Dark mode
Blue theme
Pink theme
Theme selector
Theme switching during an active game
Theme-aware game board
Theme-aware keyboard
Theme-aware game controls
Theme-aware typing area
Theme-aware surrounding frames
Organized code using separate functions
External text files for word data
🧠 Word Lists
=======
---

# ✨ Features

- Randomly selected 5-letter solutions
- 6 guesses per game
- Separate word lists for guesses and solutions
- Valid-word checking
- Duplicate-letter handling
- Green, gold, and gray letter feedback
- On-screen QWERTY keyboard
- Physical keyboard input
- Enter key support
- Keyboard color feedback
- Keyboard color priority
- Incorrect guess messages
- Remaining-guess counter
- Win detection
- Loss detection
- Game-over state
- Input disabled after the game ends
- New Game functionality
- Multiple visual themes
- Light mode
- Dark mode
- Blue theme
- Pink theme
- Theme selector
- Theme switching during an active game
- Theme-aware game board
- Theme-aware keyboard
- Theme-aware game controls
- Theme-aware typing area
- Theme-aware surrounding frames
- Organized code using separate functions
- External text files for word data

---

# 🧠 Word Lists
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

The game uses two separate word lists.

## guesses.txt

This file contains words that the player is allowed to guess.

A word can be in this file even if it is not a possible solution.

## solutions.txt

This file contains the words that the game can randomly select as the answer.

This allows the game to have a larger list of acceptable guesses while keeping the possible answers separate.

---

# 📁 Project Files

```text
Jaelyn's Practice Code/
│
├── wordle.py
├── themes.py
├── themes_ui.py
├── create_wordlist.py
├── guesses.txt
├── solutions.txt
└── README.md
```

## wordle.py

Contains the main game and the functions used to create and operate the Wordle interface.

## themes.py

Contains the color definitions for the game's themes.

## themes_ui.py

Contains the theme selector and functions used to apply themes throughout the application.

## create_wordlist.py

A utility script used to process and organize word lists.

## guesses.txt

Contains valid words that players can submit as guesses.

## solutions.txt

Contains possible words that can be selected as the game's answer.

## README.md

Contains documentation about the project.

---

# 🛠️ Technologies Used

- **Python 3**
- **Tkinter** — Used to create the graphical user interface.
- **pathlib** — Used to work with the word-list files.
- **random** — Used to randomly select a solution.
- **string.ascii_letters** — Used when filtering valid words.
- **Git / GitHub** — Used for version control.

---

# ▶️ How to Run

Make sure Python is installed on your computer.

Open the project folder in VS Code.

Open the terminal and navigate to the project folder.

Run:

```bash
python wordle.py
```

The Wordle game window should open.

---

<<<<<<< HEAD
The game supports both physical and on-screen keyboard input.
=======
# 🎯 How to Play
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

1. Start the game.
2. Enter a 5-letter word using your physical keyboard or the on-screen keyboard.
3. Press **Enter** to submit your guess.
4. Check the colors of the letters.
5. Use the feedback to improve your next guess.
6. You have a maximum of 6 valid guesses.
7. Guess the solution correctly to win.
8. If all 6 guesses are used, the game ends and the solution is revealed.
9. Click **New Game** to start another game.

---

# ⌨️ Keyboard Controls

The game supports both physical and on-screen keyboard input.

## Physical Keyboard

Type letters normally using your computer keyboard.

Press:

**Enter**

to submit a guess.

## On-Screen Keyboard

Click the letters displayed on the game's QWERTY keyboard to enter a guess.

---

# 🟩🟨⬜ Letter Feedback

The game evaluates each letter using Wordle-style rules.

## 🟩 Green

The letter is in the correct position.

**Example:**

Answer: `TWIST`

<<<<<<< HEAD
The first letter is green because T is in the correct position.
=======
Guess: `TREAT`
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

The first letter is green because T is in the correct position.

## 🟨 Gold

The letter exists somewhere in the answer but is in the wrong position.

## ⬜ Gray

The letter does not have an available match in the answer.

---

# 🔁 Duplicate Letters

The game includes logic for handling repeated letters.

When a guess contains duplicate letters, the game checks how many copies of that letter actually exist in the solution.

Correct-position matches are evaluated first.

Remaining copies of letters are then used to determine misplaced matches.

This prevents the game from incorrectly marking multiple copies of a letter as present when the solution contains fewer copies.

---

# 🎮 Game State

The game tracks whether the player is still playing using:

```python
"game_over": False
```

When the player wins or loses, the game state changes to:

```python
"game_over": True
```

Once the game is over, the guess entry is disabled.

---

# 🔄 New Game

The **New Game** feature allows the player to restart without closing the application.

Starting a new game:

- Selects a new random solution
- Clears the board
- Resets the guess counter
- Resets keyboard colors
- Clears the current guess
- Re-enables the input field
- Changes the status message back to **"Good Luck!"**

---

# 🏗️ Development Stages

The project is being developed in multiple stages.

Each stage focuses on a different part of the application. Git commits are used to track progress throughout development.

---

# Stage 1 — Core Game & Theme Functionality

<<<<<<< HEAD
Stage 1 focused on building the core Wordle game and making the theme system function correctly.

Stage 1A — Core Game

☑ Create main application window

☑ Create 6 × 5 game board

☑ Create 5-letter input

☑ Add 6-guess limit

☑ Add random solution selection

☑ Add New Game functionality

☑ Track current game row

☑ Track game-over state

Stage 1B — Word Validation & Game Logic

☑ Load solution words

☑ Load valid guess words

☑ Validate guesses

☑ Detect correct letters

☑ Detect misplaced letters

☑ Detect incorrect letters

☑ Handle duplicate letters

☑ Display win messages

☑ Display loss messages

☑ Display invalid-word messages

☑ Display remaining guesses

Stage 1C — Interactive Keyboard

☑ Create QWERTY keyboard

☑ Add clickable keyboard buttons

☑ Support physical keyboard input

☑ Add keyboard color feedback

☑ Add keyboard color priority

☑ Preserve keyboard states

Stage 1D — Theme System

☑ Create centralized theme definitions

☑ Create Light theme

☑ Create Dark theme

☑ Create Blue theme

☑ Create Pink theme

☑ Create theme selector

☑ Apply themes to application background

☑ Apply themes to text

☑ Apply themes to board

☑ Apply themes to keyboard

☑ Apply themes to game controls

Stage 1E — Theme Fixes

☑ Eliminate white keyboard/frame problem

☑ Make board borders theme correctly

☑ Make empty tiles theme correctly

☑ Preserve colored tiles when switching themes

☑ Preserve keyboard colors when switching themes

☑ Fix theme switching during an active game

☑ Make the typing area theme-aware

☑ Make the New Game button theme-aware

☑ Make surrounding frames theme-aware

Stage 2 — Wordle Visual Refinement
=======
**Status: Complete ✅**

Stage 1 focused on building the core Wordle game and making the theme system function correctly.

## Stage 1A — Core Game

- [x] Create main application window
- [x] Create 6 × 5 game board
- [x] Create 5-letter input
- [x] Add 6-guess limit
- [x] Add random solution selection
- [x] Add New Game functionality
- [x] Track current game row
- [x] Track game-over state
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

## Stage 1B — Word Validation & Game Logic

<<<<<<< HEAD
Stage 2 focuses on making the game look and feel more like the original Wordle interface.

Stage 2A — Typing Box

☐ Improve typing box appearance

☐ Adjust width

☐ Adjust height

☐ Improve border

☐ Improve font

☐ Improve text alignment

☐ Improve padding

☐ Improve cursor appearance

Stage 2B — Game Board

☐ Match Wordle tile size

☐ Refine tile spacing

☐ Refine board positioning

☐ Refine letter size

☐ Refine letter weight

☐ Refine tile borders

☐ Refine overall board proportions

Stage 2C — Keyboard

☐ Match Wordle keyboard dimensions

☐ Adjust key width

☐ Adjust key height

☐ Adjust key spacing

☐ Adjust row spacing

☐ Refine keyboard positioning

☐ Refine keyboard font

Stage 2D — Header & Controls

☐ Refine title

☐ Refine title font

☐ Refine title positioning

☐ Refine instructions

☐ Refine status message

☐ Refine New Game button

☐ Improve spacing between sections

☐ Improve overall window proportions

Stage 2E — Theme Selector

☐ Refine theme button

☐ Refine dropdown panel

☐ Improve selector spacing

☐ Improve selector typography

☐ Improve selector borders

☐ Improve selected-theme appearance

☐ Improve hover behavior

Stage 2F — Final Visual Polish

☐ Review complete application layout

☐ Refine overall proportions

☐ Refine spacing

☐ Ensure consistent typography

☐ Ensure consistent button styling

☐ Ensure consistent borders

☐ Verify all themes

☐ Compare overall appearance with Wordle

☐ Complete final UI adjustments

Stage 3 — Game Experience & Interaction
=======
- [x] Load solution words
- [x] Load valid guess words
- [x] Validate guesses
- [x] Detect correct letters
- [x] Detect misplaced letters
- [x] Detect incorrect letters
- [x] Handle duplicate letters
- [x] Display win messages
- [x] Display loss messages
- [x] Display invalid-word messages
- [x] Display remaining guesses

## Stage 1C — Interactive Keyboard
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

- [x] Create QWERTY keyboard
- [x] Add clickable keyboard buttons
- [x] Support physical keyboard input
- [x] Add keyboard color feedback
- [x] Add keyboard color priority
- [x] Preserve keyboard states

## Stage 1D — Theme System

- [x] Create centralized theme definitions
- [x] Create Light theme
- [x] Create Dark theme
- [x] Create Blue theme
- [x] Create Pink theme
- [x] Create theme selector
- [x] Apply themes to application background
- [x] Apply themes to text
- [x] Apply themes to board
- [x] Apply themes to keyboard
- [x] Apply themes to game controls

## Stage 1E — Theme Fixes

- [x] Eliminate white keyboard/frame problem
- [x] Make board borders theme correctly
- [x] Make empty tiles theme correctly
- [x] Preserve colored tiles when switching themes
- [x] Preserve keyboard colors when switching themes
- [x] Fix theme switching during an active game
- [x] Make the typing area theme-aware
- [x] Make the New Game button theme-aware
- [x] Make surrounding frames theme-aware

### 🎉 Stage 1 Complete!

The core game functionality and theme system are now working correctly across the available themes.

---

# Stage 2 — Wordle Visual Refinement

**Status: In Progress 🚧**

Stage 2 focuses on making the game look and feel more like the original Wordle interface.

## Stage 2A — Typing Box

- [ ] Improve typing box appearance
- [ ] Adjust width
- [ ] Adjust height
- [ ] Improve border
- [ ] Improve font
- [ ] Improve text alignment
- [ ] Improve padding
- [ ] Improve cursor appearance

## Stage 2B — Game Board

- [ ] Match Wordle tile size
- [ ] Refine tile spacing
- [ ] Refine board positioning
- [ ] Refine letter size
- [ ] Refine letter weight
- [ ] Refine tile borders
- [ ] Refine overall board proportions

## Stage 2C — Keyboard

- [ ] Match Wordle keyboard dimensions
- [ ] Adjust key width
- [ ] Adjust key height
- [ ] Adjust key spacing
- [ ] Adjust row spacing
- [ ] Refine keyboard positioning
- [ ] Refine keyboard font

## Stage 2D — Header & Controls

- [ ] Refine title
- [ ] Refine title font
- [ ] Refine title positioning
- [ ] Refine instructions
- [ ] Refine status message
- [ ] Refine New Game button
- [ ] Improve spacing between sections
- [ ] Improve overall window proportions

## Stage 2E — Theme Selector

- [ ] Refine theme button
- [ ] Refine dropdown panel
- [ ] Improve selector spacing
- [ ] Improve selector typography
- [ ] Improve selector borders
- [ ] Improve selected-theme appearance
- [ ] Improve hover behavior

## Stage 2F — Final Visual Polish

- [ ] Review complete application layout
- [ ] Refine overall proportions
- [ ] Refine spacing
- [ ] Ensure consistent typography
- [ ] Ensure consistent button styling
- [ ] Ensure consistent borders
- [ ] Verify all themes
- [ ] Compare overall appearance with Wordle
- [ ] Complete final UI adjustments

---

# Stage 3 — Game Experience & Interaction

**Status: Planned ⏳**

Stage 3 focuses on making the game feel more polished and interactive.

<<<<<<< HEAD
Stage 3A — Animations

☐ Add tile flip animation

☐ Add tile reveal animation

☐ Add keyboard feedback animation

☐ Add win animation

☐ Add loss animation

☐ Add invalid-word feedback animation

Stage 3B — Improved Game Feedback

☐ Improve win presentation

☐ Improve loss presentation

☐ Improve invalid-word feedback

☐ Improve game-over presentation

☐ Improve New Game transition

Stage 3C — Statistics

☐ Add games played

☐ Add wins

☐ Add losses

☐ Add win percentage

☐ Add current streak

☐ Add best streak

☐ Add guess distribution

☐ Create statistics display

Stage 3D — Accessibility & Input

☐ Improve keyboard navigation

☐ Improve focus behavior

☐ Improve physical keyboard handling

☐ Improve text readability

☐ Improve visual contrast

☐ Improve accessibility of controls

Stage 4 — Game Modes & Customization
=======
## Stage 3A — Animations
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

- [ ] Add tile flip animation
- [ ] Add tile reveal animation
- [ ] Add keyboard feedback animation
- [ ] Add win animation
- [ ] Add loss animation
- [ ] Add invalid-word feedback animation

## Stage 3B — Improved Game Feedback

- [ ] Improve win presentation
- [ ] Improve loss presentation
- [ ] Improve invalid-word feedback
- [ ] Improve game-over presentation
- [ ] Improve New Game transition

## Stage 3C — Statistics

- [ ] Add games played
- [ ] Add wins
- [ ] Add losses
- [ ] Add win percentage
- [ ] Add current streak
- [ ] Add best streak
- [ ] Add guess distribution
- [ ] Create statistics display

## Stage 3D — Accessibility & Input

- [ ] Improve keyboard navigation
- [ ] Improve focus behavior
- [ ] Improve physical keyboard handling
- [ ] Improve text readability
- [ ] Improve visual contrast
- [ ] Improve accessibility of controls

---

# Stage 4 — Game Modes & Customization

**Status: Planned ⏳**

Stage 4 focuses on expanding the game beyond the basic Wordle experience.

<<<<<<< HEAD
Stage 4A — Game Modes

☐ Add Daily Wordle mode

☐ Add Unlimited Practice mode

☐ Add Custom Word mode

☐ Add Random Practice mode

☐ Add difficulty settings

Stage 4B — Theme Customization

☐ Add additional themes

☐ Add theme persistence

☐ Save selected theme

☐ Restore selected theme when reopening the game

☐ Improve theme management

Stage 4C — Game History

☐ Save completed games

☐ Track game history

☐ Display previous results

☐ Display win/loss history

☐ Add statistics history

Stage 4D — Shareable Results

☐ Create Wordle-style result summary

☐ Add emoji tile results

☐ Add guess count

☐ Add copy-to-clipboard functionality

☐ Add shareable result format

Stage 5 — Sound, Settings & Final Polish
=======
## Stage 4A — Game Modes
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

- [ ] Add Daily Wordle mode
- [ ] Add Unlimited Practice mode
- [ ] Add Custom Word mode
- [ ] Add Random Practice mode
- [ ] Add difficulty settings

## Stage 4B — Theme Customization

- [ ] Add additional themes
- [ ] Add theme persistence
- [ ] Save selected theme
- [ ] Restore selected theme when reopening the game
- [ ] Improve theme management

## Stage 4C — Game History

- [ ] Save completed games
- [ ] Track game history
- [ ] Display previous results
- [ ] Display win/loss history
- [ ] Add statistics history

## Stage 4D — Shareable Results

- [ ] Create Wordle-style result summary
- [ ] Add emoji tile results
- [ ] Add guess count
- [ ] Add copy-to-clipboard functionality
- [ ] Add shareable result format

---

# Stage 5 — Sound, Settings & Final Polish

**Status: Planned ⏳**

Stage 5 focuses on optional enhancements and preparing the project for a final release.

<<<<<<< HEAD
Stage 5A — Sound

☐ Add optional sound effects

☐ Add keyboard sound

☐ Add tile reveal sound

☐ Add win sound

☐ Add loss sound

☐ Add sound toggle

Stage 5B — Settings

☐ Create settings menu

☐ Add sound settings

☐ Add animation settings

☐ Add theme settings

☐ Add accessibility settings

☐ Save user preferences

Stage 5C — Final Polish

☐ Review all game functionality

☐ Review all themes

☐ Review animations

☐ Review keyboard interaction

☐ Review statistics

☐ Review settings

☐ Fix remaining bugs

☐ Improve error handling

☐ Clean up code

☐ Remove unnecessary code

☐ Improve documentation

☐ Perform final testing

🧩 Project Structure
=======
## Stage 5A — Sound

- [ ] Add optional sound effects
- [ ] Add keyboard sound
- [ ] Add tile reveal sound
- [ ] Add win sound
- [ ] Add loss sound
- [ ] Add sound toggle

## Stage 5B — Settings

- [ ] Create settings menu
- [ ] Add sound settings
- [ ] Add animation settings
- [ ] Add theme settings
- [ ] Add accessibility settings
- [ ] Save user preferences

## Stage 5C — Final Polish

- [ ] Review all game functionality
- [ ] Review all themes
- [ ] Review animations
- [ ] Review keyboard interaction
- [ ] Review statistics
- [ ] Review settings
- [ ] Fix remaining bugs
- [ ] Improve error handling
- [ ] Clean up code
- [ ] Remove unnecessary code
- [ ] Improve documentation
- [ ] Perform final testing

---

# 🧩 Project Structure
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

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

---

# 📚 What This Project Practices

This project is being used to practice several Python programming concepts, including:

<<<<<<< HEAD
Functions
Function parameters
Return values
Variables
Constants
Dictionaries
Lists
Sets
Loops
Conditional statements
if, elif, and else
for loops
enumerate()
Lambda functions
Dictionary lookups
String manipulation
File handling
List comprehensions
Set comprehensions
Random selection
GUI development with Tkinter
Tkinter widgets
Event handling
Keyboard events
GUI state management
Git version control
GitHub
🚧 Future Improvements

Possible future features include:

Statistics tracking
Win percentage
Current streak
Best streak
Guess distribution
Animated letter reveals
Start screen
Instructions/help screen
Game reset confirmation
Daily Wordle mode
Shareable results
Sound effects
More polished animations
👩🏽‍💻 Author
=======
- Functions
- Function parameters
- Return values
- Variables
- Constants
- Dictionaries
- Lists
- Sets
- Loops
- Conditional statements
- `if`, `elif`, and `else`
- `for` loops
- `enumerate()`
- Lambda functions
- Dictionary lookups
- String manipulation
- File handling
- List comprehensions
- Set comprehensions
- Random selection
- GUI development with Tkinter
- Tkinter widgets
- Event handling
- Keyboard events
- GUI state management
- Git version control
- GitHub

---

# 🚧 Future Improvements

Possible future features include:

- Statistics tracking
- Win percentage
- Current streak
- Best streak
- Guess distribution
- Animated letter reveals
- Start screen
- Instructions/help screen
- Game reset confirmation
- Daily Wordle mode
- Shareable results
- Sound effects
- More polished animations
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

---

# 👩🏽‍💻 Author

**Jaelyn Garrard**

This project was created as a hands-on Python programming project to practice building a complete graphical application from the ground up.

---

# 📌 Project Status

**Currently in development.**

## Development Progress

<<<<<<< HEAD
Stage 2 — Wordle Visual Refinement: 🚧 In Progress
=======
| Stage | Status |
|---|---|
| Stage 1 — Core Game & Theme Functionality | ✅ Complete |
| Stage 2 — Wordle Visual Refinement | 🚧 In Progress |
| Stage 3 — Game Experience & Interaction | ⏳ Planned |
| Stage 4 — Game Modes & Customization | ⏳ Planned |
| Stage 5 — Sound, Settings & Final Polish | ⏳ Planned |
>>>>>>> 7a376bae39e25593bad1e01f7cd927b623178a23

New features and improvements will be added as the project continues.
