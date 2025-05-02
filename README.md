# Python Mini Projects Collection

This repository contains a collection of six mini Python projects, each focusing on different types of functionality, from games to utilities and web scraping. These projects are designed to be fun, educational, and practical for beginner to intermediate Python learners.

## Projects Overview

### Category 1: Web Scraping
- **scrape_imdb.py**  
  A web scraper that fetches IMDb's Top 250 movies, along with their release dates, lengths, ratings, and votes.

### Category 2: Games
- **simple_quiz.py**  
  An interactive trivia quiz game that pulls questions from the [Open Trivia Database API](https://opentdb.com/). Players can select the number of questions, answer them, and get their score at the end.
  
- **rps_game.py**  
  A classic Rock, Paper, Scissors game that allows you to play against the computer. It tracks scores and displays results after each round.
  
- **fruity_loops.py (Hangman Game)**  
  A fruit-themed Hangman game with a colorful terminal interface. The goal is to guess the fruit name before running out of moves!

### Category 3: Utilities
- **pass_generator.py**  
  A customizable password generator that lets you specify whether to include uppercase, lowercase, digits, or symbols. It can generate multiple random passwords at once.
  
- **bill_calculator.py**  
  A bill calculator that calculates tips, splits the total among multiple people, and rewards credits. It also allows users to confirm or decline the generated totals.

## Dependencies

Before running the projects, you'll need to install the following dependencies:
```bash
pip install requests beautifulsoup4
```

These dependencies are used for web scraping (requests and BeautifulSoup) and for making HTTP requests in some projects.

## Colorized Terminal Output

Some projects also use `color_prt.py` to add color to the terminal output. You don’t need any external dependencies for this; it’s all handled through ANSI escape codes for color formatting.

## Utility Module

Several projects rely on `input_tools.py` for user input validation and handling, such as ensuring that numbers are correctly inputted.

## File Descriptions

### `color_prt.py`
This utility file provides the `print()` function, which prints colored text to the terminal. Supported colors include: `red`, `green`, `yellow`, `blue`, `purple`, `cyan`, and `white`.

### `input_tools.py`
Contains functions for handling user input:
- `get_int(msg)`: Prompts the user for an integer input, with validation.
- `get_float(msg)`: Prompts the user for a float input, with validation.
- `get_menu_selection(msg, min, max)`: Prompts the user to select an option from a menu, ensuring that the input is within a specified range.

### `ascii_chars.py`
Contains predefined lists of characters that are commonly used in password generation, including uppercase, lowercase, digits, and symbols.

### `cmn_pass.py`
Contains a list of common passwords that are checked against the generated passwords to ensure their strength.

## Acknowledgements

- Open Trivia Database for the trivia API used in the quiz game.
- IMDb for providing movie data.
