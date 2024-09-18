
import random
import os


class BattleshipGame:
    """
    A class to represent a Battleship game.
    """

    def __init__(self, size, num_ships, player_name, ship_type):
        """
        Initialize the game with grid size, number of ships, player name,
        and ship type. Also, create the grid and randomly place ships
        on it for both player and computer.
        """
        self.size = size
        self.num_ships = num_ships
        self.player_name = player_name
        self.ship_type = ship_type
        self.player_grid = self.create_grid()
        self.computer_grid = self.create_grid()
        self.player_ships = self.place_ships(self.player_grid)
        self.computer_ships = self.place_ships(self.computer_grid)
        self.player_guesses = []
        self.computer_guesses = []

    def create_grid(self):
        """
        Create an empty game grid of the specified size.
        """
        return [["O" for _ in range(self.size)] for _ in range(self.size)]

    def place_ships(self, grid):
        """
        Randomly place the specified number of ships on the grid.
        Ensures that no two ships occupy the same coordinates.
        """
        ships = []
        while len(ships) < self.num_ships:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in ships:
                ships.append((row, col))
                grid[row][col] = "X"
        return ships

    def display_grid(self, grid, hide_ships=False):
        """
        Display the current state of the grid to the player.
        The grid will show hits "H", misses "M", and unexplored spots "O".
        If hide_ships is True, the ships "X" will not be displayed.
        """
        for row in grid:
            display_row = []
            for cell in row:
                if hide_ships and cell == "X":
                    display_row.append("O")
                else:
                    display_row.append(cell)
            print(" ".join(display_row))
        print()

    def get_player_guess(self):
        """
        Prompt the player to enter coordinates for their guess.
        Ensures that the input is valid and within the grid's bounds.
        """
        while True:
            try:
                row = input(f"Enter a row (0-{self.size - 1}): ")
                col = input(f"Enter a column (0-{self.size - 1}): ")

                # Validate that the input is a single-digit number
                if (
                    row.isdigit() and col.isdigit() and
                    len(row) == 1 and len(col) == 1 and
                    0 <= int(row) < self.size and
                    0 <= int(col) < self.size
                ):

                    row, col = int(row), int(col)

                    if (row, col) not in self.player_guesses:
                        self.player_guesses.append((row, col))
                        return row, col
                    else:
                        print("You've already guessed those coordinates! "
                              "Try again.")
                else:
                    print("Invalid input! Please enter a single digit for "
                          "both row and column.")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

    def check_guess(self, grid, ships, guess):
        """
        Check if the guess hits or misses a ship. Marks the grid accordingly
        with "H" for hits and "M" for misses.
        """
        row, col = guess
        if (row, col) in ships:
            print("Hit!")
            grid[row][col] = "H"
            ships.remove((row, col))
        else:
            print("Miss!")
            grid[row][col] = "M"

    def check_game_over(self, ships):
        """
        Check if all ships have been sunk, indicating that the game is over.
        """
        return not ships

    def computer_turn(self):
        """
        Generate a random guess for the computer.
        Ensure that the computer doesn't guess the same spot twice.
        """
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in self.computer_guesses:
                self.computer_guesses.append((row, col))
                return (row, col)

    def start_game(self):
        """
        Start the game, display the grids, and manage the game loop.
        The game continues until all ships are hit and the player
        or computer wins.
        """
        clear_console()
        print(f"Welcome, {self.player_name}! Let's play Battleships!\n")
        print(
            f"Grid Size: {self.size}x{self.size}, "
            f"Ships: {self.num_ships}, Ship Type: {self.ship_type}"
        )
        print("Here is your game board:\n")
        self.display_grid(self.player_grid)

        while True:
            # Player's turn
            print("\nYour turn:")
            player_guess = self.get_player_guess()
            self.check_guess(self.computer_grid,
                             self.computer_ships, player_guess)

            if self.check_game_over(self.computer_ships):
                print("\nCongratulations! You've sunk all the computer's "
                      "ships!")
                break

            # Computer's turn
            print("\nComputer's turn:")
            computer_guess = self.computer_turn()
            print(f"Computer guesses: {computer_guess}")
            self.check_guess(self.player_grid,
                             self.player_ships, computer_guess)

            if self.check_game_over(self.player_ships):
                print("\nGame over! The computer has sunk all your ships!")
                break

            print("\nYour board:")
            self.display_grid(self.player_grid)
            print("\nComputer's board:")
            self.display_grid(self.computer_grid, hide_ships=True)

        self.end_game_menu()

    def end_game_menu(self):
        """
        Display a menu at the end of the game with options to restart or return
        to the home page.
        """
        while True:
            print("\nGame Over! What would you like to do?")
            print("1. Restart Game")
            print("2. Return to Home Page")
            choice = input("Enter 1 or 2: ")

            if choice == "1":
                self.restart_game()
                break
            elif choice == "2":
                show_home_page()
                break
            else:
                print("Invalid choice, please try again.")

    def restart_game(self):
        """
        Restart the game with the same settings.
        """
        self.__init__(self.size, self.num_ships, self.player_name,
                      self.ship_type)
        self.start_game()


def show_instructions():
    """
    Display instructions on how to play the game.
    """
    clear_console()
    print("Instructions:")
    print("1. This is a simple Battleships game.")
    print("2. You and the computer will each have a grid.")
    print("3. Your goal is to guess where the computer's ships are.")
    print("4. You will be prompted to enter row and column coordinates.")
    print("5. Hits will be marked with 'H' and misses with 'M'.")
    print("6. The game ends when all ships of either side are sunk.")
    input("\nPress Enter to return to the home screen.")
    show_home_page()


def show_home_page():
    """
    Display the home page with options to start the game or view instructions.
    """
    clear_console()
    # ASCII Art
    print(r"""
     ____        _   _   _           _     _           _
    | __ )  __ _| |_| |_| | ___  ___| |__ (_)_ __  ___| |
    |  _ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __| |
    | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ \_|
    |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___(_)
                                            |_|
    """)

    print("Welcome to Battleships!\n")
    print("1. Start Game\n")
    print("2. Instructions\n")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        player_name = input("Enter your name to start the game: ").strip()

        # Input validation: Ensure name is not empty or just spaces
        while not player_name:
            print("Invalid name. Please enter a valid name to start the game.")
            player_name = input("Enter your name to start the game: ").strip()

        game = BattleshipGame(
            size=5,
            num_ships=4,
            player_name=player_name,
            ship_type="Battleship"
        )
        game.start_game()
    elif choice == "2":
        show_instructions()
    else:
        print("Invalid choice. Please try again.")
        show_home_page()


def clear_console():
    """
    Clear the console for better readability.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    show_home_page()
