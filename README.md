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

- Home Screen: The game features an interactive home screen with options to start the game or view detailed instructions on how to play. It also includes input validation to ensure that only the correct options are selected.

- Player vs. Computer Gameplay: Players compete against a computer opponent, taking turns to guess the location of each other's ships. The game keeps track of both the player's and computer's moves, providing a challenging experience.

- Random Ship Placement: Ships are randomly placed on both the player's and computer's grids at the start of the game, ensuring a unique game experience each time. The placement logic prevents any overlap between ships.

- Real-time Feedback: During gameplay, hits ("H"), misses ("M"), and the status of the ships are displayed in real-time on the grid. This provides clear and immediate feedback to the player about their progress.

### Input Validation:

- Home Screen: Input validation ensures that players can only select valid options (1 or 2) when choosing to start the game or view instructions.

- Player Name: Players must enter a valid name to start the game, ensuring they cannot proceed without providing an appropriate input.

- Coordinate Input: The game validates that players input single-digit row and column values within the grid's range, preventing invalid entries during their turns.

- End Game Menu: Once the game concludes (whether the player wins or loses), an end-game menu is displayed, offering options to either restart the game or return to the home screen. Input validation ensures that players make a valid selection at this stage.

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

![home page](docs/images/home.png)

- The home page of the Battleships game displays a welcome message and ASCII art. The player is prompted to choose between two options: "1. Start Game" to begin playing or "2. Instructions" to learn how to play.

![instructions](docs/images/instructions.png)

- The instructions screen provides detailed steps on how to play the Battleships game. It explains the goal, the game rules, and the player's objective. This screen is displayed when the player selects the "Instructions" option from the home page.

![instructions input validation](docs/images/instructions-validation.png)

- This screenshot shows the input validation feature on the instructions screen. If a player enters an incorrect key (anything other than "1"), an error message prompts them to enter "1" to return to the home screen, ensuring proper input validation and user guidance.

### Battleships Game 
![enter name to start game](docs/images/enter-name.png)

- This screen prompts the player to enter their name before starting the game. It ensures that every player provides their name to personalize the game experience.

![invalid choice](docs/images/input-home.png)

- When a player enters an invalid input (anything other than "1" or "2") on the home screen, an error message appears, instructing them to enter either "1" to start the game or "2" to view the instructions.


![invalid name](docs/images/invalid-name.png)

- This screen shows input validation when the player attempts to start the game without entering a valid name. An error message prompts the player to provide a name, ensuring they do not proceed with an empty or whitespace-only entry.

![start of game](docs/images/start-of-game.png)

- This screenshot shows the beginning of the game after the player has entered their name. It displays the player's grid and provides details such as the grid size, the number of ships, and the ship type.

![computer unhidden ships](docs/images/unhide-ships.png)

- For testing purposes, this screenshot displays the computer's grid with ships unhidden. This feature helps verify ship placements during game development but is not part of the standard gameplay.

![duplicated turn](docs/images/duplicated-turn.png)

This screenshot demonstrates the input validation for repeated guesses. When the player tries to guess the same coordinates multiple times, an error message appears, instructing them to pick a new location.

![correct turn](docs/images/correct-turn.png)

- This screen shows that the player has entered valid coordinates correctly to play the game. However, the guess results in a "Miss," indicated by the "M" on the grid, showing that no ship was hit.

![incorrect turn](docs/images/invalid-turn.png)

- This screenshot demonstrates the input validation feature in action. The player has entered invalid coordinates, and the game displays an error message, prompting them to enter valid coordinates within the grid's boundaries.

![loser](docs/images/loser-end.png)

- This screen appears when the player loses the game. The computer has sunk all the player's ships, and the game ends with a "Game over!" message.

![winner](docs/images/winner-end.png)

- This screenshot displays the end-of-game screen when the player wins. It congratulates the player for successfully sinking all the computer's ships and winning the game.

![input validation at the end of the game ](docs/images/end-game-validation.png)

- This screen demonstrates the input validation feature at the end of the game. If the player enters an invalid key when prompted to either restart the game or return to the home page, an error message appears, instructing them to enter "1" or "2" to make a valid choice.

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
### Flake8 and PEP8

Code has been run through flake8 to ensure it follows PEP8 guidelines, fixing issues with line lengths and formatting.

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

- [Youtube: Corey Schafer] (https://www.youtube.com/watch?v=ZDa-Z5JzLYM) A comprehensive guide on creating classes in Python. 

- [YouTube: How to Fix] (https://www.youtube.com/watch?v=Zt1G6AE_7Ks) A helpful guide on resolving issues with lines that exceed the recommended length in Python code.

- DeftStack (https://www.delftstack.com/howto/python/python-clear-console/#google_vignette) Instructions on how to clear the console in Python.

- ASCII Art Archive (https://www.asciiart.eu/text-to-ascii-art) Used for adding Battleships! ASCII art to the home page.