import random
import os  # For clearing the console


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
                row = int(input(f"Enter a row (0-{self.size - 1}): "))
                col = int(input(f"Enter a column (0-{self.size - 1}): "))
                if ((row, col) not in self.player_guesses and
                        0 <= row < self.size and 0 <= col < self.size):
                    self.player_guesses.append((row, col))
                    return (row, col)
                elif (row, col) in self.player_guesses:
                    print(
                        "You've already guessed those coordinates! Try again."
                    )
                else:
                    print("Invalid input! Enter values within the grid range.")
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
        print(f"Grid Size: {self.size}x{self.size}, Ships: {self.num_ships}, "
              f"Ship Type: {self.ship_type}")
        print("Here is your game board:\n")
        self.display_grid(self.player_grid)

        while True:
            # Player's turn
            print("\nYour turn:")
            self.display_grid(self.computer_grid, hide_ships=True)
            player_guess = self.get_player_guess()
            self.check_guess(self.computer_grid,
                             self.computer_ships, player_guess)

            if self.check_game_over(self.computer_ships):
                print(
                    "\nCongratulations! You've sunk all the computer's ships!"
                )
                self.end_of_game_menu()
                break

            # Computer's turn
            print("\nComputer's turn:")
            computer_guess = self.computer_turn()
            print(f"Computer guesses: {computer_guess}")
            self.check_guess(self.player_grid,
                             self.player_ships, computer_guess)

            if self.check_game_over(self.player_ships):
                print("\nGame over! The computer has sunk all your ships!")
                self.end_of_game_menu()
                break

            print("\nYour board:")
            self.display_grid(self.player_grid)
            print("\nComputer's board:")
            self.display_grid(self.computer_grid, hide_ships=True)

    def end_of_game_menu(self):
        """
        Display a menu after the game ends to restart or quit to the home page.
        """
        while True:
            print("\nGame Over! What would you like to do next?")
            print("1. Press 'R' to restart the game.")
            print("2. Press 'H' to return to the home page.")
            choice = input("\nEnter your choice: ").strip().upper()

            if choice == 'R':
                self.__init__(self.size, self.num_ships, self.player_name, self.ship_type)
                self.start_game()
                break
            elif choice == 'H':
                show_home_page()
                break
            else:
                print("Invalid choice. Please try again.")


def clear_console():
    """
    Clear the console screen based on the user's operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def show_home_page():
    """
    Display the home page with options to start the game or quit.
    """
    clear_console()
    print("Welcome to the Battleship Game!")
    print("1. Press 'S' to start the game.")
    
    while True:
        choice = input("\nEnter your choice: ").strip().upper()
        if choice == 'S':
            player_name = input("Enter your name to start the game: ")
            game = BattleshipGame(size=5, num_ships=4, player_name=player_name,
                                  ship_type="Battleship")
            game.start_game()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    show_home_page()