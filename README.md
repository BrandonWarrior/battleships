![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


# Battleships! - Project 3

The Battleship Game is a Python-based console game where the player competes against the computer. Each player has a grid where ships are placed randomly. The goal of the game is to guess the locations of the opponent's ships and sink them before your ships are sunk.

## Features

- Home Screen: The game now features a home screen with options to start the game or view instructions on how to play.

- Player vs. Computer: The player and computer take turns guessing the location of each other's ships.

- Random Ship Placement: Ships are placed randomly on the grids for both the player and the computer, with no overlap between ships.

- Guess Validation: The game ensures that the player's guesses are valid, preventing out-of-bound entries or previously guessed coordinates.

- Input Validation: Players must enter their name before the game can begin, and invalid choices on the home screen are caught and handled appropriately.

- Feedback: Hits, misses, and sunk ships are displayed in real-time during the game.

- End Game Menu: When the game is over, players are presented with an option to restart the game or return to the home screen.

## Game Rules 

- The player and the computer take turns guessing the location of each other's ships.

- The goal is to sink all of the opponent's ships before your own fleet is destroyed.

- Ships are placed randomly on the grid.

- Players are prompted to input row and column values to guess where the opponent's ships are.

- Hits will be marked as "H", misses as "M", and unexplored spots as "O".

## How to Play

- Upon launching, the player is presented with a home screen where they can either start the game or view instructions on how to play.

- After selecting the "Start Game" option, the player is asked to enter their name, and the game begins.

- The player takes turns guessing the location of the computer's ships by entering row and column coordinates, and the computer does the same for the player's grid.

- The game continues until one side sinks all the ships.


## Example Gameplay

### Instructions 
![]()

![]()

### Battleships Game 
![]()

![]()

![]()

![]()

![]()

## Future Enhancements 

- Allow the player to choose the number of ships.

- Implement different types of ships with varying sizes.

- Allow the player to choose grid size. 

## Code Structure 

- BattleshipGame: The main class responsible for managing the game.

- create_grid: Creates an empty game grid.

- place_ships: Randomly places ships on the grid.

- display_grid: Displays the current state of the grid.

- get_player_guess: Prompts the player for valid input.

- check_guess: Checks whether a guess is a hit or miss and updates the grid accordingly.

- computer_turn: Generates a random guess for the computer.

- start_game: Manages the game loop, alternating between player and computer turns.

- end_game_menu: Displays options to either restart the game or return to the home screen.

## Validation
### Flake8

Code has been run through flake8 to ensure it follows PEP8 guidelines, fixing issues with line lengths and formatting.

### PEP8


## Deployment

Deployment
To deploy this Battleship game on Heroku, follow these steps:

-  Fork or Clone the Repository

- Create a New Heroku App
- Log in to Heroku.
- Click "New" > "Create New App".
- Name your app and select your region.

- Set Buildpacks
- Go to the Settings tab on Heroku.
- Under Buildpacks, add Python first, then Node.js.
- create a Config Var called PORT. Set this to 8000

- Link the Repository and Enable Automatic Deploys In the Deploy tab.
- select GitHub as the deployment method.
- Search for your GitHub repository and connect it.
- Click deploy. 

- App is live at: https://battleships-project3-4a1230ee998c.herokuapp.com/

## Bugs and Fixes

- Invalid Input Handling: Resolved a bug where users could input multiple digits in the row/column inputs. Input validation now ensures only single-digit inputs are accepted.

- Player's Grid Displayed Twice: Fixed the issue where the player's grid was displayed twice after each turn.

- Input Validation for Player Names: Fixed a bug where players could start the game without entering a name or entering just spaces.

- Input Validation: Resolved an issue where the invalid input message on the home screen would not appear properly when entering an incorrect key. Now, the game properly displays an error message and waits for a valid input (1 or 2) before proceeding.

## Credits

- Code institute for the project 3 scope video. 

- [Youtube: Corey Schafer] (https://www.youtube.com/watch?v=ZDa-Z5JzLYM) for creating classes in python. 

- [YouTube: How to Fix] (https://www.youtube.com/watch?v=Zt1G6AE_7Ks) for how to fix lines too long. 

- DeftStack (https://www.delftstack.com/howto/python/python-clear-console/#google_vignette) for how to clear console in Python.

- ASCII Art Archive (https://www.asciiart.eu/text-to-ascii-art) for adding Battleships! art to home page. 