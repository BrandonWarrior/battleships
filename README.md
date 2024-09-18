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

- Player vs. Computer: The player and computer take turns guessing the location of each other's ships.

- Random Ship Placement: Both player and computer ships are placed randomly on their respective grids.

- Guess Validation: The game ensures that the player's guesses are valid and within the grid boundaries.

- Feedback: Hits, misses, and sunk ships are displayed in real-time during the game.

## Game Rules 

- Player vs. Computer: The player and computer take turns guessing the location of each other's ships.

- Random Ship Placement: Both player and computer ships are placed randomly on their respective grids.

- Guess Validation: The game ensures that the player's guesses are valid and within the grid boundaries.

- Feedback: Hits, misses, and sunk ships are displayed in real-time during the game.

## How to Play

- The game begins by asking the player to enter their name.

- The player and the computer each have a grid with ships placed randomly.

- The player takes turns guessing the location of the computer's ships by entering row and column coordinates.

- The computer also guesses the player's ship locations.

- The game continues until either the player or the computer sinks all of the opponent's ships.


## Example Gameplay

## Future Enhancements 

- Allow the player to choose the number of ships.

- Implement different types of ships with varying sizes.

- Allow the player to choose grid size. 

## Code Structure 

- BattleshipGame: The main class responsible for managing the game.

- create_grid: Creates an empty game grid.

- place_ships: Randomly places ships on the grid.

- display_grid: Displays the current state of the grid.

- get_player_guess: Gets valid input from the player.

- check_guess: Checks whether a guess is a hit or miss.

- computer_turn: Generates a random guess for the computer.

- start_game: Manages the game loop, alternating between player and computer turns.

## Validation
### Flake8 
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

- Link the Repository and Enable Automatic Deploys
In the Deploy tab, select GitHub as the deployment method.
- Search for your GitHub repository and connect it.
- Click deploy. 

- App is live at: https://battleships-project3-4a1230ee998c.herokuapp.com/

## Bugs and Fixes

- 

## Credits

- Code institute for the project 3 scope video. 

- [Youtube: Corey Schafer] (https://www.youtube.com/watch?v=ZDa-Z5JzLYM) for creating classes in python. 

- [YouTube: How to Fix] (https://www.youtube.com/watch?v=Zt1G6AE_7Ks) for how to fix lines too long. 

