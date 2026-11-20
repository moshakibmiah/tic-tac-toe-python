# Tic Tac Toe (Python)

A two-player console game with numbered squares, input validation, turn switching, and detection of wins and draws. Built with functions and conditional logic using the Python standard library.

## Run

Install Python 3.10 or later, then run from this folder:

```sh
python tic_tac_toe.py
```

On Windows, `py tic_tac_toe.py` also works if the Python launcher is installed. No extra packages are required.

## How to play

- Two people share a keyboard. X always starts.
- Enter a number from 1 to 9 to claim an empty square.
- Complete a row, column, or diagonal to win.
- A full board with no winner is a draw.
- Enter `q` at a move prompt to quit, or `y` after a game to play again.
- Invalid or occupied squares do not use up a turn.

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## Test

```sh
python -m unittest discover -v
```

The tests cover every winning line for both players, a draw, valid moves, and invalid input that must leave the board unchanged. GitHub Actions runs the tests on Python 3.10 and 3.13.

## Code guide

- `display_board`: renders available square numbers and player marks.
- `make_move`: validates a selection before changing the board.
- `winner`: checks the eight possible winning lines.
- `play_game`: manages turns and the end of a round.
- `main`: handles replay and a clean exit.

This is a local console game; it has no online multiplayer or computer opponent.
