# TicTacToe Game Package

## Overview

This package provides a Python implementation of the classic TicTacToe game. The core of the package is the `TicTacToe` class, which encapsulates the game's state and logic. The class manages the board and the moves made by the players but leaves the implementation of the game's playing logic (e.g., taking turns, handling user input) to the user of the package.

## Key Features

- Tracks the game state including each player's moves.
- Checks for valid moves and win conditions.
- Supports playing the game via a command-line interface.

## Usage

To play TicTacToe from the command line, first ensure the package is installed. Then, you can start a game session by running the following commands in your Python environment:

```python
from tictactoe import command_line_game
command_line_game()
```